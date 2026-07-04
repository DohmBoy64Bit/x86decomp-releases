# Authorized static test bundles

A test bundle is the preferred way to provide a real regression target without asking
the toolkit to execute an uploaded Windows program. It is a ZIP archive with a root
`x86decomp-test-bundle.json` manifest and hash-listed artifacts.

## Best bundle contents

The strongest practical bundle contains:

1. `target.exe` or `target.dll` — an unpacked native Windows PE image that the uploader
   owns or is authorized to analyze. PE32/i386 is the preferred first target; PE32+
   AMD64 is also supported.
2. The matching linker `.map` — this supplies public addresses, object ownership, entry
   point, preferred base, and sometimes contribution evidence.
3. Matching `.obj` files from the same link — these supply original COFF relocations,
   auxiliary symbols, COMDAT selection, TLS subsections, initializer subsections, and
   section checksums that the linked image no longer retains.
4. The matching `.pdb`, when available — the bundle runner seals its hash, parses the
   bounded MSF/PDB/TPI/IPI/DBI inventory, and checks GUID/age against the PE RSDS
   record. Complete CodeView type and symbol records are not claimed.
5. A rebuilt image as `candidate_image`, with the original listed as
   `reference_image`, for target-specific whole-image comparison.
6. Known source, compiler profile, compiler/linker version text, flags, and a short
   README explaining provenance and the intended checks.

A bare authorized `.exe` or `.dll` is still useful for PE parsing, section/import/
resource/TLS/debug analysis, RTTI, vtable, exception/unwind, and whole-image profile
creation. The `.map` and `.obj` files are what unlock deeper linker reconstruction.

## Create a bundle

The CLI calculates all hashes and writes deterministic archive member metadata:

```bash
x86decomp test-bundle-create authorized-target.zip \
  --name "Authorized game build 1.0" \
  --expected-architecture x86 \
  --authorization "I own these artifacts or have permission to analyze them." \
  --artifact primary_image=target.exe \
  --artifact linker_map=target.map \
  --artifact pdb=target.pdb \
  --artifact coff_object=obj/main.obj \
  --artifact coff_object=obj/render.obj
```

For whole-image comparison:

```bash
x86decomp test-bundle-create image-pair.zip \
  --authorization "Authorized private regression artifacts." \
  --artifact reference_image=original.exe \
  --artifact candidate_image=rebuilt.exe \
  --artifact image_profile=original-image-profile.json
```

## Inspect a bundle

```bash
x86decomp test-bundle-inspect authorized-target.zip \
  --report reports/test-bundle.json
```

The inspector performs only static operations:

- verifies the archive and artifact hashes;
- parses PE images;
- scans bounded MSVC RTTI, vtables, unwind/EH, TLS, and initializer evidence;
- parses classic COFF and bigobj objects plus bounded static/import archives;
- parses supplied PDB identity, TPI/IPI headers, DBI modules, contributions, and source mappings;
- resolves COMDAT groups;
- parses an MSVC-compatible map and reconstructs evidenced layout relationships;
- compares reference/candidate images when both are supplied.

It does **not** execute an EXE, DLL, object, library, source file, or script from the
bundle.

## Manifest contract

The root manifest follows `schemas/test-bundle.schema.json`:

```json
{
  "schema_version": 1,
  "name": "authorized-target",
  "expected_architecture": "x86",
  "authorization": {
    "owner_or_authorized": true,
    "statement": "I own these artifacts or have permission to analyze them."
  },
  "artifacts": [
    {
      "path": "files/target.exe",
      "role": "primary_image",
      "sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"
    }
  ]
}
```

Supported roles:

- `primary_image`
- `reference_image`
- `candidate_image`
- `pdb`
- `linker_map`
- `coff_object`
- `static_library`
- `source`
- `compiler_profile`
- `image_profile`
- `documentation`

## Archive guardrails

The inspector rejects:

- absolute paths;
- `..` components;
- backslash or drive-qualified paths;
- duplicate members;
- symbolic links;
- oversized files or total expansion;
- excessive compression ratios;
- undeclared/missing artifact files;
- artifact hash mismatches;
- a manifest without an affirmative authorization statement.

Parser success is not a malware-safety determination and is not proof of semantic
equivalence. Do not upload malware, packed DRM-protected software, credentials,
private keys, or proprietary artifacts you are not permitted to share.
