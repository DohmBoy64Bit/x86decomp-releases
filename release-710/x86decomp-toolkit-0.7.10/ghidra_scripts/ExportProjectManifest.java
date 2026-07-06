// Export canonical program, section, function, symbol, and metric manifests.
// Usage: -postScript ExportProjectManifest.java <output-dir>
// @category X86Decomp

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.*;
import ghidra.program.model.data.DataType;
import ghidra.program.model.data.DataTypeManager;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.MemoryBlock;
import ghidra.program.model.symbol.*;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.security.MessageDigest;
import java.util.*;

public class ExportProjectManifest extends GhidraScript {
    private File outputRoot;
    private Address imageBase;

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 1 || args[0].trim().isEmpty()) {
            throw new IllegalArgumentException("ExportProjectManifest requires <output-dir>");
        }
        outputRoot = new File(args[0]).getCanonicalFile();
        if (!outputRoot.exists() && !outputRoot.mkdirs()) {
            throw new IOException("Unable to create output directory: " + outputRoot);
        }
        imageBase = currentProgram.getImageBase();

        writeProgram();
        writeSections();
        Metrics metrics = writeFunctions();
        writeSymbols();
        writeTypes();
        writeMetrics(metrics);
        println("ExportProjectManifest: wrote manifests to " + outputRoot);
    }

    private void writeProgram() throws Exception {
        String executablePath = currentProgram.getExecutablePath();
        String executableSha256 = null;
        Long executableSize = null;
        if (executablePath != null) {
            File executable = new File(executablePath);
            if (executable.isFile()) {
                executableSha256 = sha256(executable);
                executableSize = executable.length();
            }
        }

        StringBuilder sb = new StringBuilder();
        sb.append("{\n");
        field(sb, "schema_version", "1", false, 2);
        field(sb, "program_name", json(currentProgram.getName()), false, 2);
        field(sb, "executable_path", json(executablePath), false, 2);
        field(sb, "executable_sha256", json(executableSha256), false, 2);
        field(sb, "executable_size", executableSize == null ? "null" : executableSize.toString(), false, 2);
        field(sb, "executable_format", json(currentProgram.getExecutableFormat()), false, 2);
        field(sb, "language_id", json(currentProgram.getLanguageID().toString()), false, 2);
        field(sb, "compiler_spec_id", json(currentProgram.getCompilerSpec().getCompilerSpecID().toString()), false, 2);
        field(sb, "image_base", json(imageBase.toString()), false, 2);
        field(sb, "min_address", json(currentProgram.getMinAddress().toString()), false, 2);
        field(sb, "max_address", json(currentProgram.getMaxAddress().toString()), true, 2);
        sb.append("}\n");
        writeText(new File(outputRoot, "program.json"), sb.toString());
    }

    private void writeSections() throws Exception {
        MemoryBlock[] blocks = currentProgram.getMemory().getBlocks();
        StringBuilder sb = new StringBuilder();
        sb.append("{\n  \"schema_version\": 1,\n  \"blocks\": [\n");
        for (int i = 0; i < blocks.length; i++) {
            MemoryBlock block = blocks[i];
            sb.append("    {");
            sb.append("\"name\": ").append(json(block.getName())).append(", ");
            sb.append("\"start\": ").append(json(block.getStart().toString())).append(", ");
            sb.append("\"end_inclusive\": ").append(json(block.getEnd().toString())).append(", ");
            sb.append("\"size\": ").append(block.getSize()).append(", ");
            sb.append("\"initialized\": ").append(block.isInitialized()).append(", ");
            sb.append("\"read\": ").append(block.isRead()).append(", ");
            sb.append("\"write\": ").append(block.isWrite()).append(", ");
            sb.append("\"execute\": ").append(block.isExecute()).append(", ");
            sb.append("\"volatile\": ").append(block.isVolatile()).append(", ");
            sb.append("\"source_name\": ").append(json(block.getSourceName()));
            sb.append("}");
            if (i + 1 < blocks.length) sb.append(",");
            sb.append("\n");
        }
        sb.append("  ]\n}\n");
        writeText(new File(outputRoot, "sections.json"), sb.toString());
    }

    private Metrics writeFunctions() throws Exception {
        Metrics metrics = new Metrics();
        File file = new File(outputRoot, "functions.jsonl");
        try (PrintWriter out = writer(file)) {
            FunctionIterator iterator = currentProgram.getFunctionManager().getFunctions(true);
            while (iterator.hasNext()) {
                if (monitor.isCancelled()) break;
                Function function = iterator.next();
                metrics.total++;
                if (function.isExternal()) metrics.external++;
                if (function.isThunk()) metrics.thunks++;
                if (function.getSymbol().getSource() == SourceType.DEFAULT) metrics.defaultNamed++;
                else metrics.nonDefaultNamed++;

                long rva = unsignedDifference(function.getEntryPoint(), imageBase);
                int incomingReferences = countReferencesTo(function.getEntryPoint());
                StringBuilder sb = new StringBuilder();
                sb.append("{");
                sb.append("\"schema_version\":1,");
                sb.append("\"id\":").append(json(String.format("pe-rva:%08x", rva))).append(",");
                sb.append("\"entry\":").append(json(function.getEntryPoint().toString())).append(",");
                sb.append("\"entry_rva\":").append(rva).append(",");
                sb.append("\"entry_rva_hex\":").append(json(String.format("0x%08x", rva))).append(",");
                sb.append("\"name\":").append(json(function.getName())).append(",");
                sb.append("\"name_source\":").append(json(function.getSymbol().getSource().toString())).append(",");
                sb.append("\"calling_convention\":").append(json(function.getCallingConventionName())).append(",");
                sb.append("\"return_type\":").append(json(function.getReturnType().getDisplayName())).append(",");
                sb.append("\"signature\":").append(json(function.getSignature().getPrototypeString())).append(",");
                sb.append("\"is_external\":").append(function.isExternal()).append(",");
                sb.append("\"is_thunk\":").append(function.isThunk()).append(",");
                Function thunked = function.getThunkedFunction(false);
                sb.append("\"thunk_target\":").append(json(thunked == null ? null : thunked.getEntryPoint().toString())).append(",");
                sb.append("\"incoming_reference_count\":").append(incomingReferences).append(",");
                sb.append("\"address_count\":").append(function.getBody().getNumAddresses()).append(",");
                sb.append("\"body_ranges\":[");
                AddressRangeIterator ranges = function.getBody().getAddressRanges();
                boolean firstRange = true;
                int rangeCount = 0;
                while (ranges.hasNext()) {
                    AddressRange range = ranges.next();
                    if (!firstRange) sb.append(",");
                    firstRange = false;
                    rangeCount++;
                    long startRva = unsignedDifference(range.getMinAddress(), imageBase);
                    long endRva = unsignedDifference(range.getMaxAddress(), imageBase) + 1;
                    sb.append("{");
                    sb.append("\"start\":").append(json(range.getMinAddress().toString())).append(",");
                    Address endExclusive = range.getMaxAddress().next();
                    sb.append("\"end_exclusive\":").append(json(endExclusive == null ? null : endExclusive.toString())).append(",");
                    sb.append("\"start_rva\":").append(startRva).append(",");
                    sb.append("\"end_rva\":").append(endRva);
                    sb.append("}");
                }
                if (rangeCount > 1) metrics.multiRangeFunctions++;
                sb.append("],");
                sb.append("\"parameters\":[");
                Parameter[] parameters = function.getParameters();
                for (int i = 0; i < parameters.length; i++) {
                    Parameter parameter = parameters[i];
                    if (i > 0) sb.append(",");
                    sb.append("{");
                    sb.append("\"ordinal\":").append(parameter.getOrdinal()).append(",");
                    sb.append("\"name\":").append(json(parameter.getName())).append(",");
                    sb.append("\"type\":").append(json(parameter.getDataType().getDisplayName())).append(",");
                    sb.append("\"storage\":").append(json(parameter.getVariableStorage().toString()));
                    sb.append("}");
                }
                sb.append("]");
                sb.append("}");
                out.println(sb.toString());
            }
        }
        return metrics;
    }

    private void writeSymbols() throws Exception {
        File file = new File(outputRoot, "symbols.jsonl");
        try (PrintWriter out = writer(file)) {
            SymbolIterator iterator = currentProgram.getSymbolTable().getSymbolIterator();
            while (iterator.hasNext()) {
                if (monitor.isCancelled()) break;
                Symbol symbol = iterator.next();
                StringBuilder sb = new StringBuilder();
                sb.append("{");
                sb.append("\"schema_version\":1,");
                sb.append("\"name\":").append(json(symbol.getName())).append(",");
                sb.append("\"qualified_name\":").append(json(symbol.getName(true))).append(",");
                sb.append("\"address\":").append(json(symbol.getAddress().toString())).append(",");
                sb.append("\"type\":").append(json(symbol.getSymbolType().toString())).append(",");
                sb.append("\"source\":").append(json(symbol.getSource().toString())).append(",");
                sb.append("\"primary\":").append(symbol.isPrimary()).append(",");
                sb.append("\"dynamic\":").append(symbol.isDynamic()).append(",");
                sb.append("\"external\":").append(symbol.isExternal());
                sb.append("}");
                out.println(sb.toString());
            }
        }
    }

    private void writeTypes() throws Exception {
        File file = new File(outputRoot, "types.jsonl");
        DataTypeManager manager = currentProgram.getDataTypeManager();
        try (PrintWriter out = writer(file)) {
            Iterator<DataType> iterator = manager.getAllDataTypes();
            while (iterator.hasNext()) {
                if (monitor.isCancelled()) break;
                DataType type = iterator.next();
                StringBuilder sb = new StringBuilder();
                sb.append("{");
                sb.append("\"schema_version\":1,");
                sb.append("\"name\":").append(json(type.getName())).append(",");
                sb.append("\"path_name\":").append(json(type.getPathName())).append(",");
                sb.append("\"category_path\":").append(json(type.getCategoryPath().toString())).append(",");
                sb.append("\"class\":").append(json(type.getClass().getName())).append(",");
                sb.append("\"length\":").append(type.getLength()).append(",");
                sb.append("\"description\":").append(json(type.getDescription()));
                sb.append("}");
                out.println(sb.toString());
            }
        }
    }

    private void writeMetrics(Metrics metrics) throws Exception {
        StringBuilder sb = new StringBuilder();
        sb.append("{\n");
        field(sb, "schema_version", "1", false, 2);
        field(sb, "total_functions", Integer.toString(metrics.total), false, 2);
        field(sb, "external_functions", Integer.toString(metrics.external), false, 2);
        field(sb, "thunks", Integer.toString(metrics.thunks), false, 2);
        field(sb, "default_named_functions", Integer.toString(metrics.defaultNamed), false, 2);
        field(sb, "non_default_named_functions", Integer.toString(metrics.nonDefaultNamed), false, 2);
        field(sb, "multi_range_functions", Integer.toString(metrics.multiRangeFunctions), true, 2);
        sb.append("}\n");
        writeText(new File(outputRoot, "metrics.json"), sb.toString());
    }

    private int countReferencesTo(Address address) {
        int count = 0;
        ReferenceIterator iterator = currentProgram.getReferenceManager().getReferencesTo(address);
        while (iterator.hasNext()) {
            iterator.next();
            count++;
        }
        return count;
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

    private String sha256(File file) throws Exception {
        MessageDigest digest = MessageDigest.getInstance("SHA-256");
        try (InputStream in = Files.newInputStream(file.toPath())) {
            byte[] buffer = new byte[1024 * 1024];
            int count;
            while ((count = in.read(buffer)) != -1) {
                digest.update(buffer, 0, count);
            }
        }
        StringBuilder sb = new StringBuilder();
        for (byte b : digest.digest()) sb.append(String.format("%02x", b & 0xff));
        return sb.toString();
    }

    private void field(StringBuilder sb, String key, String value, boolean last, int indent) {
        sb.append(" ".repeat(indent)).append(json(key)).append(": ").append(value);
        if (!last) sb.append(",");
        sb.append("\n");
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

    private static class Metrics {
        int total;
        int external;
        int thunks;
        int defaultNamed;
        int nonDefaultNamed;
        int multiRangeFunctions;
    }
}
