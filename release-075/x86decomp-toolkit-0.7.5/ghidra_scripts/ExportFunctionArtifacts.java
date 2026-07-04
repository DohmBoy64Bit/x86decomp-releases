// Export per-function artifacts without flattening discontiguous bodies.
// Usage: -postScript ExportFunctionArtifacts.java <output-dir> <all|current|addr,name,...>
// @category X86Decomp

import ghidra.app.decompiler.*;
import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.*;
import ghidra.program.model.data.DataType;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.MemoryAccessException;
import ghidra.program.model.pcode.HighFunction;
import ghidra.program.model.pcode.PcodeOp;
import ghidra.program.model.pcode.PcodeOpAST;
import ghidra.program.model.pcode.Varnode;
import ghidra.program.model.symbol.*;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.*;

public class ExportFunctionArtifacts extends GhidraScript {
    private File outputRoot;
    private File functionsRoot;
    private Address imageBase;
    private DecompInterface decompiler;
    private Listing listing;
    private ReferenceManager references;
    private FunctionManager functions;

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 1 || args[0].trim().isEmpty()) {
            throw new IllegalArgumentException("ExportFunctionArtifacts requires <output-dir>");
        }
        String selector = args.length >= 2 ? args[1].trim() : "current";
        outputRoot = new File(args[0]).getCanonicalFile();
        functionsRoot = new File(outputRoot, "functions");
        if (!functionsRoot.exists() && !functionsRoot.mkdirs()) {
            throw new IOException("Unable to create functions directory: " + functionsRoot);
        }
        imageBase = currentProgram.getImageBase();
        listing = currentProgram.getListing();
        references = currentProgram.getReferenceManager();
        functions = currentProgram.getFunctionManager();

        decompiler = new DecompInterface();
        DecompileOptions options = new DecompileOptions();
        decompiler.setOptions(options);
        decompiler.toggleCCode(true);
        decompiler.toggleSyntaxTree(true);
        if (!decompiler.openProgram(currentProgram)) {
            throw new IOException("Unable to open current program in the decompiler");
        }

        List<Function> selected = selectFunctions(selector);
        int succeeded = 0;
        int failed = 0;
        try {
            for (Function function : selected) {
                if (monitor.isCancelled()) break;
                try {
                    exportFunction(function);
                    succeeded++;
                } catch (Exception exc) {
                    failed++;
                    printerr("Failed " + function.getName() + " @ " + function.getEntryPoint() + ": " + exc);
                }
            }
        } finally {
            decompiler.dispose();
        }
        println("ExportFunctionArtifacts: " + succeeded + " succeeded, " + failed + " failed");
        if (failed > 0) {
            throw new IOException("One or more function exports failed");
        }
    }

    private List<Function> selectFunctions(String selector) {
        LinkedHashMap<String, Function> selected = new LinkedHashMap<>();
        if (selector.equalsIgnoreCase("all")) {
            FunctionIterator iterator = functions.getFunctions(true);
            while (iterator.hasNext()) {
                Function function = iterator.next();
                if (!function.isExternal()) selected.put(function.getEntryPoint().toString(), function);
            }
            return new ArrayList<>(selected.values());
        }
        if (selector.equalsIgnoreCase("current")) {
            if (currentAddress == null) {
                throw new IllegalArgumentException("current selection is unavailable in this headless context");
            }
            Function function = functions.getFunctionContaining(currentAddress);
            if (function == null || function.isExternal()) {
                throw new IllegalArgumentException("cursor is not inside a non-external function");
            }
            return Collections.singletonList(function);
        }
        for (String raw : selector.split(",")) {
            String token = raw.trim();
            if (token.isEmpty()) continue;
            Function function = findFunction(token);
            if (function == null || function.isExternal()) {
                throw new IllegalArgumentException("Unable to resolve non-external function: " + token);
            }
            selected.put(function.getEntryPoint().toString(), function);
        }
        if (selected.isEmpty()) throw new IllegalArgumentException("selector resolved no functions");
        return new ArrayList<>(selected.values());
    }

    private Function findFunction(String token) {
        try {
            String clean = token.startsWith("0x") || token.startsWith("0X") ? token.substring(2) : token;
            Address address = currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(clean);
            Function function = functions.getFunctionAt(address);
            if (function == null) function = functions.getFunctionContaining(address);
            if (function != null) return function;
        } catch (Exception ignored) {
        }
        FunctionIterator iterator = functions.getFunctions(true);
        while (iterator.hasNext()) {
            Function function = iterator.next();
            if (function.getName().equals(token) || function.getName(true).equals(token)) return function;
        }
        return null;
    }

    private void exportFunction(Function function) throws Exception {
        long rva = unsignedDifference(function.getEntryPoint(), imageBase);
        String id = String.format("pe-rva:%08x", rva);
        File directory = new File(functionsRoot, id.replace(':', '_'));
        File rangesDirectory = new File(directory, "ranges");
        if (!rangesDirectory.exists() && !rangesDirectory.mkdirs()) {
            throw new IOException("Unable to create artifact directory: " + rangesDirectory);
        }

        List<RangeRecord> rangeRecords = exportRanges(function, rangesDirectory);
        DecompileResults result = decompiler.decompileFunction(function, 120, monitor);
        writeDecompilation(directory, result);
        writeDecompilerTree(directory, result);
        writePcode(directory, function, result);
        writeInstructions(directory, function);
        writeReferences(directory, function);
        writeConservativeContext(directory, function);
        writeFunctionManifest(directory, function, id, rva, rangeRecords, result);
    }

    private List<RangeRecord> exportRanges(Function function, File rangesDirectory) throws Exception {
        List<RangeRecord> records = new ArrayList<>();
        AddressRangeIterator iterator = function.getBody().getAddressRanges();
        int index = 0;
        while (iterator.hasNext()) {
            AddressRange range = iterator.next();
            long lengthLong = range.getLength();
            if (lengthLong > Integer.MAX_VALUE) {
                throw new IOException("Function body range exceeds supported artifact size");
            }
            int length = (int)lengthLong;
            byte[] bytes = new byte[length];
            int read = currentProgram.getMemory().getBytes(range.getMinAddress(), bytes);
            if (read != length) throw new IOException("Short memory read for " + range);
            String fileName = String.format("%02d_%s_%s.bin", index, range.getMinAddress(), range.getMaxAddress());
            try (OutputStream out = new BufferedOutputStream(new FileOutputStream(new File(rangesDirectory, fileName)))) {
                out.write(bytes);
            }
            records.add(new RangeRecord(
                range.getMinAddress(),
                range.getMaxAddress(),
                unsignedDifference(range.getMinAddress(), imageBase),
                unsignedDifference(range.getMaxAddress(), imageBase) + 1,
                fileName,
                length
            ));
            index++;
        }
        return records;
    }

    private void writeDecompilation(File directory, DecompileResults result) throws IOException {
        String text;
        if (result != null && result.decompileCompleted() && result.getDecompiledFunction() != null) {
            text = result.getDecompiledFunction().getC();
        } else {
            String message = result == null ? "no result" : result.getErrorMessage();
            text = "/* Ghidra decompilation did not complete: " + safeComment(message) + " */\n";
        }
        writeText(new File(directory, "decompiler.c"), text == null ? "" : text);
    }


    private void writeDecompilerTree(File directory, DecompileResults result) throws IOException {
        File file = new File(directory, "decompiler-tree.jsonl");
        try (PrintWriter out = writer(file)) {
            if (result == null || !result.decompileCompleted()) return;
            ClangTokenGroup root = result.getCCodeMarkup();
            if (root == null) return;
            int[] nextId = new int[] {0};
            writeDecompilerNode(out, root, -1, nextId);
        }
    }

    private void writeDecompilerNode(PrintWriter out, ClangNode node, int parentId, int[] nextId) {
        int id = nextId[0]++;
        Address min = node.getMinAddress();
        Address max = node.getMaxAddress();
        String text = node instanceof ClangToken ? ((ClangToken) node).getText() : null;
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        sb.append("\"id\":").append(id).append(",");
        sb.append("\"parent_id\":").append(parentId < 0 ? "null" : Integer.toString(parentId)).append(",");
        sb.append("\"node_class\":").append(json(node.getClass().getName())).append(",");
        sb.append("\"text\":").append(json(text)).append(",");
        sb.append("\"min_address\":").append(json(min == null ? null : min.toString())).append(",");
        sb.append("\"max_address\":").append(json(max == null ? null : max.toString())).append(",");
        sb.append("\"child_count\":").append(node.numChildren());
        sb.append("}");
        out.println(sb.toString());
        for (int i = 0; i < node.numChildren(); i++) {
            ClangNode child = node.Child(i);
            if (child != null) writeDecompilerNode(out, child, id, nextId);
        }
    }

    private void writePcode(File directory, Function function, DecompileResults result) throws IOException {
        File highText = new File(directory, "high-pcode.txt");
        File highJson = new File(directory, "high-pcode.jsonl");
        try (PrintWriter textOut = writer(highText); PrintWriter jsonOut = writer(highJson)) {
            if (result == null || !result.decompileCompleted()) {
                textOut.println("# unavailable: decompilation did not complete");
            } else {
                HighFunction high = result.getHighFunction();
                if (high == null) {
                    textOut.println("# unavailable: no HighFunction");
                } else {
                    Iterator<PcodeOpAST> iterator = high.getPcodeOps();
                    int index = 0;
                    while (iterator.hasNext()) {
                        PcodeOpAST op = iterator.next();
                        textOut.println(op.toString());
                        jsonOut.println(pcodeJson(op, index++, "high"));
                    }
                }
            }
        }

        File rawJson = new File(directory, "raw-pcode.jsonl");
        try (PrintWriter out = writer(rawJson)) {
            InstructionIterator instructions = listing.getInstructions(function.getBody(), true);
            int index = 0;
            while (instructions.hasNext()) {
                Instruction instruction = instructions.next();
                PcodeOp[] ops = instruction.getPcode();
                for (PcodeOp op : ops) {
                    String record = pcodeJson(op, index++, "raw");
                    record = record.substring(0, record.length() - 1) + ",\"instruction_address\":" + json(instruction.getAddress().toString()) + "}";
                    out.println(record);
                }
            }
        }
    }

    private String pcodeJson(PcodeOp op, int index, String level) {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        sb.append("\"index\":").append(index).append(",");
        sb.append("\"level\":").append(json(level)).append(",");
        sb.append("\"mnemonic\":").append(json(op.getMnemonic())).append(",");
        sb.append("\"sequence\":").append(json(op.getSeqnum().toString())).append(",");
        sb.append("\"output\":").append(varnodeJson(op.getOutput())).append(",");
        sb.append("\"inputs\":[");
        for (int i = 0; i < op.getNumInputs(); i++) {
            if (i > 0) sb.append(",");
            sb.append(varnodeJson(op.getInput(i)));
        }
        sb.append("]}");
        return sb.toString();
    }

    private String varnodeJson(Varnode value) {
        if (value == null) return "null";
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        sb.append("\"text\":").append(json(value.toString())).append(",");
        sb.append("\"address\":").append(json(value.getAddress() == null ? null : value.getAddress().toString())).append(",");
        sb.append("\"offset\":").append(value.getOffset()).append(",");
        sb.append("\"size\":").append(value.getSize()).append(",");
        sb.append("\"constant\":").append(value.isConstant()).append(",");
        sb.append("\"register\":").append(value.isRegister()).append(",");
        sb.append("\"unique\":").append(value.isUnique()).append(",");
        sb.append("\"address_tied\":").append(value.isAddrTied());
        sb.append("}");
        return sb.toString();
    }

    private void writeInstructions(File directory, Function function) throws IOException {
        File jsonl = new File(directory, "instructions.jsonl");
        File assembly = new File(directory, "listing.asm");
        try (PrintWriter jsonOut = writer(jsonl); PrintWriter asmOut = writer(assembly)) {
            InstructionIterator iterator = listing.getInstructions(function.getBody(), true);
            while (iterator.hasNext()) {
                Instruction instruction = iterator.next();
                byte[] bytes;
                try {
                    bytes = instruction.getBytes();
                } catch (MemoryAccessException exc) {
                    bytes = new byte[0];
                }
                asmOut.printf("%s  %-32s  %s%n", instruction.getAddress(), hex(bytes), instruction.toString());
                StringBuilder sb = new StringBuilder();
                sb.append("{");
                sb.append("\"address\":").append(json(instruction.getAddress().toString())).append(",");
                sb.append("\"rva\":").append(unsignedDifference(instruction.getAddress(), imageBase)).append(",");
                sb.append("\"bytes_hex\":").append(json(hex(bytes).replace(" ", ""))).append(",");
                sb.append("\"mnemonic\":").append(json(instruction.getMnemonicString())).append(",");
                sb.append("\"text\":").append(json(instruction.toString())).append(",");
                sb.append("\"flow_type\":").append(json(instruction.getFlowType().toString())).append(",");
                sb.append("\"fallthrough\":").append(json(instruction.getFallThrough() == null ? null : instruction.getFallThrough().toString())).append(",");
                sb.append("\"flows\":[");
                Address[] flows = instruction.getFlows();
                for (int i = 0; i < flows.length; i++) {
                    if (i > 0) sb.append(",");
                    sb.append(json(flows[i].toString()));
                }
                sb.append("],\"operands\":[");
                for (int i = 0; i < instruction.getNumOperands(); i++) {
                    if (i > 0) sb.append(",");
                    sb.append(json(instruction.getDefaultOperandRepresentation(i)));
                }
                sb.append("]}");
                jsonOut.println(sb.toString());
            }
        }
    }

    private void writeReferences(File directory, Function function) throws IOException {
        File file = new File(directory, "references.jsonl");
        try (PrintWriter out = writer(file)) {
            AddressIterator addresses = function.getBody().getAddresses(true);
            while (addresses.hasNext()) {
                Address from = addresses.next();
                Reference[] refs = references.getReferencesFrom(from);
                for (Reference ref : refs) {
                    Function destinationFunction = functions.getFunctionAt(ref.getToAddress());
                    StringBuilder sb = new StringBuilder();
                    sb.append("{");
                    sb.append("\"from\":").append(json(ref.getFromAddress().toString())).append(",");
                    sb.append("\"to\":").append(json(ref.getToAddress().toString())).append(",");
                    sb.append("\"type\":").append(json(ref.getReferenceType().toString())).append(",");
                    sb.append("\"operand_index\":").append(ref.getOperandIndex()).append(",");
                    sb.append("\"source\":").append(json(ref.getSource().toString())).append(",");
                    sb.append("\"primary\":").append(ref.isPrimary()).append(",");
                    sb.append("\"destination_function\":").append(json(destinationFunction == null ? null : destinationFunction.getName(true)));
                    sb.append("}");
                    out.println(sb.toString());
                }
            }
        }
    }

    private void writeConservativeContext(File directory, Function function) throws IOException {
        File file = new File(directory, "context.h");
        try (PrintWriter out = writer(file)) {
            out.println("#pragma once");
            out.println("#include <stdint.h>");
            out.println();
            out.println("/* Analysis-derived declaration. Types and calling convention remain unverified until evidence promotes them. */");
            out.println("/* Ghidra signature: " + safeComment(function.getSignature().getPrototypeString()) + " */");
            out.println("/* Calling convention guess: " + safeComment(function.getCallingConventionName()) + " */");
            out.println();
            out.println("/* Referenced symbols are intentionally not assigned guessed C types here. */");
        }
    }

    private void writeFunctionManifest(
        File directory,
        Function function,
        String id,
        long rva,
        List<RangeRecord> ranges,
        DecompileResults result
    ) throws IOException {
        StringBuilder sb = new StringBuilder();
        sb.append("{\n");
        sb.append("  \"schema_version\": 2,\n");
        sb.append("  \"selected_modes\": [\"matching\", \"functional\"],\n");
        sb.append("  \"matching_status\": \"decompiled\",\n");
        sb.append("  \"functional_status\": \"decompiled\",\n");
        sb.append("  \"id\": ").append(json(id)).append(",\n");
        sb.append("  \"entry\": ").append(json(function.getEntryPoint().toString())).append(",\n");
        sb.append("  \"entry_rva\": ").append(rva).append(",\n");
        sb.append("  \"name\": ").append(json(function.getName())).append(",\n");
        sb.append("  \"qualified_name\": ").append(json(function.getName(true))).append(",\n");
        sb.append("  \"name_source\": ").append(json(function.getSymbol().getSource().toString())).append(",\n");
        sb.append("  \"calling_convention\": ").append(json(function.getCallingConventionName())).append(",\n");
        sb.append("  \"signature\": ").append(json(function.getSignature().getPrototypeString())).append(",\n");
        sb.append("  \"return_type\": ").append(json(function.getReturnType().getDisplayName())).append(",\n");
        sb.append("  \"is_thunk\": ").append(function.isThunk()).append(",\n");
        sb.append("  \"decompile_completed\": ").append(result != null && result.decompileCompleted()).append(",\n");
        sb.append("  \"decompile_error\": ").append(json(result == null ? "no result" : result.getErrorMessage())).append(",\n");
        sb.append("  \"artifacts\": {\"decompiler_c\":\"decompiler.c\",\"decompiler_tree\":\"decompiler-tree.jsonl\",\"high_pcode\":\"high-pcode.jsonl\",\"raw_pcode\":\"raw-pcode.jsonl\",\"instructions\":\"instructions.jsonl\",\"references\":\"references.jsonl\"},\n");
        sb.append("  \"body_ranges\": [\n");
        for (int i = 0; i < ranges.size(); i++) {
            RangeRecord range = ranges.get(i);
            sb.append("    {");
            sb.append("\"start\":").append(json(range.start.toString())).append(",");
            sb.append("\"end_inclusive\":").append(json(range.endInclusive.toString())).append(",");
            sb.append("\"start_rva\":").append(range.startRva).append(",");
            sb.append("\"end_rva\":").append(range.endRva).append(",");
            sb.append("\"size\":").append(range.size).append(",");
            sb.append("\"file\":").append(json("ranges/" + range.fileName));
            sb.append("}");
            if (i + 1 < ranges.size()) sb.append(",");
            sb.append("\n");
        }
        sb.append("  ],\n");
        sb.append("  \"parameters\": [");
        Parameter[] parameters = function.getParameters();
        for (int i = 0; i < parameters.length; i++) {
            if (i > 0) sb.append(",");
            Parameter parameter = parameters[i];
            sb.append("{");
            sb.append("\"ordinal\":").append(parameter.getOrdinal()).append(",");
            sb.append("\"name\":").append(json(parameter.getName())).append(",");
            sb.append("\"type\":").append(json(parameter.getDataType().getDisplayName())).append(",");
            sb.append("\"storage\":").append(json(parameter.getVariableStorage().toString()));
            sb.append("}");
        }
        sb.append("]\n}");
        writeText(new File(directory, "function.json"), sb.toString() + "\n");
    }

    private long unsignedDifference(Address address, Address base) {
        return address.subtract(base) & 0xffffffffL;
    }

    private PrintWriter writer(File file) throws IOException {
        return new PrintWriter(new OutputStreamWriter(new FileOutputStream(file), StandardCharsets.UTF_8));
    }

    private void writeText(File file, String text) throws IOException {
        try (PrintWriter out = writer(file)) {
            out.print(text);
        }
    }

    private String hex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bytes.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(String.format("%02X", bytes[i] & 0xff));
        }
        return sb.toString();
    }

    private String safeComment(String value) {
        if (value == null) return "";
        return value.replace("*/", "* /").replace("\r", " ").replace("\n", " ");
    }

    private String json(String value) {
        if (value == null) return "null";
        StringBuilder sb = new StringBuilder("\"");
        for (int i = 0; i < value.length(); i++) {
            char c = value.charAt(i);
            switch (c) {
                case '\\': sb.append("\\\\"); break;
                case '"': sb.append("\\\""); break;
                case '\b': sb.append("\\b"); break;
                case '\f': sb.append("\\f"); break;
                case '\n': sb.append("\\n"); break;
                case '\r': sb.append("\\r"); break;
                case '\t': sb.append("\\t"); break;
                default:
                    if (c < 0x20) sb.append(String.format("\\u%04x", (int)c));
                    else sb.append(c);
            }
        }
        return sb.append('"').toString();
    }

    private static class RangeRecord {
        final Address start;
        final Address endInclusive;
        final long startRva;
        final long endRva;
        final String fileName;
        final int size;

        RangeRecord(Address start, Address endInclusive, long startRva, long endRva, String fileName, int size) {
            this.start = start;
            this.endInclusive = endInclusive;
            this.startRva = startRva;
            this.endRva = endRva;
            this.fileName = fileName;
            this.size = size;
        }
    }
}
