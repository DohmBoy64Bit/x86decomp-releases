// Read-only Ghidra analysis queries.
// Commands:
//   QueryAnalysis.java refs <address> [all|read|write|call]
//   QueryAnalysis.java disasm <start> <end-exclusive>
//   QueryAnalysis.java function <address-or-name>
//   QueryAnalysis.java callers <address-or-name>
// @category X86Decomp

import ghidra.app.script.GhidraScript;
import ghidra.program.model.address.*;
import ghidra.program.model.listing.*;
import ghidra.program.model.mem.MemoryAccessException;
import ghidra.program.model.symbol.*;

import java.util.*;

public class QueryAnalysis extends GhidraScript {
    private FunctionManager functions;
    private ReferenceManager references;
    private Listing listing;

    @Override
    public void run() throws Exception {
        String[] args = getScriptArgs();
        if (args.length < 2) {
            throw new IllegalArgumentException("Expected: refs|disasm|function|callers plus arguments");
        }
        functions = currentProgram.getFunctionManager();
        references = currentProgram.getReferenceManager();
        listing = currentProgram.getListing();
        String command = args[0].toLowerCase(Locale.ROOT);
        switch (command) {
            case "refs":
                queryReferences(parseAddress(args[1]), args.length >= 3 ? args[2] : "all");
                break;
            case "disasm":
                if (args.length < 3) throw new IllegalArgumentException("disasm requires start and end-exclusive");
                queryDisassembly(parseAddress(args[1]), parseAddress(args[2]));
                break;
            case "function":
                queryFunction(requireFunction(args[1]));
                break;
            case "callers":
                queryCallers(requireFunction(args[1]));
                break;
            default:
                throw new IllegalArgumentException("Unknown command: " + command);
        }
    }

    private void queryReferences(Address target, String filterRaw) {
        String filter = filterRaw.toLowerCase(Locale.ROOT);
        if (!Arrays.asList("all", "read", "write", "call").contains(filter)) {
            throw new IllegalArgumentException("Reference filter must be all, read, write, or call");
        }
        ReferenceIterator iterator = references.getReferencesTo(target);
        while (iterator.hasNext()) {
            Reference reference = iterator.next();
            RefType type = reference.getReferenceType();
            if (filter.equals("read") && !type.isRead()) continue;
            if (filter.equals("write") && !type.isWrite()) continue;
            if (filter.equals("call") && !type.isCall()) continue;
            Function containing = functions.getFunctionContaining(reference.getFromAddress());
            println("{" +
                "\"target\":" + json(target.toString()) + "," +
                "\"from\":" + json(reference.getFromAddress().toString()) + "," +
                "\"type\":" + json(type.toString()) + "," +
                "\"operand_index\":" + reference.getOperandIndex() + "," +
                "\"source\":" + json(reference.getSource().toString()) + "," +
                "\"containing_function\":" + json(containing == null ? null : containing.getName(true)) +
                "}");
        }
    }

    private void queryDisassembly(Address start, Address endExclusive) {
        if (start.compareTo(endExclusive) >= 0) {
            throw new IllegalArgumentException("start must be below end-exclusive");
        }
        InstructionIterator iterator = listing.getInstructions(start, true);
        while (iterator.hasNext()) {
            Instruction instruction = iterator.next();
            if (instruction.getAddress().compareTo(endExclusive) >= 0) break;
            byte[] bytes;
            try {
                bytes = instruction.getBytes();
            } catch (MemoryAccessException exc) {
                bytes = new byte[0];
            }
            println("{" +
                "\"address\":" + json(instruction.getAddress().toString()) + "," +
                "\"bytes_hex\":" + json(hex(bytes).replace(" ", "")) + "," +
                "\"mnemonic\":" + json(instruction.getMnemonicString()) + "," +
                "\"text\":" + json(instruction.toString()) + "," +
                "\"flow_type\":" + json(instruction.getFlowType().toString()) +
                "}");
        }
    }

    private void queryFunction(Function function) {
        StringBuilder sb = new StringBuilder();
        sb.append("{");
        sb.append("\"entry\":").append(json(function.getEntryPoint().toString())).append(",");
        sb.append("\"name\":").append(json(function.getName(true))).append(",");
        sb.append("\"signature\":").append(json(function.getSignature().getPrototypeString())).append(",");
        sb.append("\"calling_convention\":").append(json(function.getCallingConventionName())).append(",");
        sb.append("\"is_external\":").append(function.isExternal()).append(",");
        sb.append("\"is_thunk\":").append(function.isThunk()).append(",");
        sb.append("\"body_ranges\":[");
        AddressRangeIterator ranges = function.getBody().getAddressRanges();
        boolean first = true;
        while (ranges.hasNext()) {
            AddressRange range = ranges.next();
            if (!first) sb.append(",");
            first = false;
            sb.append("{");
            sb.append("\"start\":").append(json(range.getMinAddress().toString())).append(",");
            sb.append("\"end_inclusive\":").append(json(range.getMaxAddress().toString()));
            sb.append("}");
        }
        sb.append("]}");
        println(sb.toString());
    }

    private void queryCallers(Function function) {
        ReferenceIterator iterator = references.getReferencesTo(function.getEntryPoint());
        while (iterator.hasNext()) {
            Reference reference = iterator.next();
            if (!reference.getReferenceType().isCall()) continue;
            Function caller = functions.getFunctionContaining(reference.getFromAddress());
            println("{" +
                "\"callee\":" + json(function.getName(true)) + "," +
                "\"call_site\":" + json(reference.getFromAddress().toString()) + "," +
                "\"caller\":" + json(caller == null ? null : caller.getName(true)) + "," +
                "\"reference_type\":" + json(reference.getReferenceType().toString()) +
                "}");
        }
    }

    private Function requireFunction(String token) {
        try {
            Address address = parseAddress(token);
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
        throw new IllegalArgumentException("Unable to resolve function: " + token);
    }

    private Address parseAddress(String token) {
        String clean = token.trim();
        if (clean.startsWith("0x") || clean.startsWith("0X")) clean = clean.substring(2);
        return currentProgram.getAddressFactory().getDefaultAddressSpace().getAddress(clean);
    }

    private String hex(byte[] bytes) {
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < bytes.length; i++) {
            if (i > 0) sb.append(' ');
            sb.append(String.format("%02X", bytes[i] & 0xff));
        }
        return sb.toString();
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
}
