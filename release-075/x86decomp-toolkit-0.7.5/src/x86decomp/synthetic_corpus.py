"""Deterministic ground-truth source corpus generation.

The generator expands a small, reviewed family of source templates into a
configurable set of C and C++ translation units.  Every generated file is
content-hashed and described by parameters in a manifest.  The output is
source evidence only: generation does not claim that any compiler, optimization
level, or resulting binary has been tested until ``ground-truth-build`` records
a successful build.
"""

from __future__ import annotations

import random
import re
from pathlib import Path
from typing import Any, Callable

from .errors import ContractError
from .util import sha256_file, utc_now, write_json

GENERATOR_SCHEMA_VERSION = 1
_IDENTIFIER = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")


def _symbol(case_id: str) -> str:
    value = re.sub(r"[^A-Za-z0-9_]", "_", case_id)
    if not value or value[0].isdigit():
        value = "case_" + value
    if not _IDENTIFIER.match(value):
        raise ContractError(f"unable to derive a C identifier from case id: {case_id}")
    return value


def _c_arithmetic(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    a, b, c = (rng.randrange(3, 251) | 1 for _ in range(3))
    shift = rng.randrange(1, 16)
    return f"""/* generated deterministic arithmetic case */
unsigned {fn}(unsigned x, unsigned y) {{
    unsigned v = (x * {a}u) + (y ^ {b}u);
    v = (v << {shift}) | (v >> {32-shift});
    return (v ^ (x + {c}u)) + (y * {a+b}u);
}}
"""


def _c_branches(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    thresholds = sorted(rng.sample(range(-500, 501), 5))
    values = [rng.randrange(-2000, 2001) for _ in range(6)]
    conditions = "\n".join(
        f"    if (x < {threshold}) return {values[index]};"
        for index, threshold in enumerate(thresholds)
    )
    return f"""/* generated deterministic branch case */
int {fn}(int x) {{
{conditions}
    return {values[-1]};
}}
"""


def _c_loop(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    multiplier = rng.randrange(3, 97)
    bias = rng.randrange(1, 101)
    mask = (1 << rng.randrange(8, 31)) - 1
    return f"""/* generated deterministic bounded loop case */
unsigned {fn}(const unsigned *values, unsigned count) {{
    unsigned acc = {bias}u;
    unsigned i;
    for (i = 0; i < count; ++i) {{
        acc = ((acc ^ values[i]) * {multiplier}u) & {mask}u;
    }}
    return acc;
}}
"""


def _c_switch(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    labels = sorted(rng.sample(range(0, 64), 10))
    returns = [rng.randrange(-500, 501) for _ in labels]
    cases = "\n".join(f"        case {label}: return {value};" for label, value in zip(labels, returns))
    return f"""/* generated deterministic switch case */
int {fn}(unsigned selector) {{
    switch (selector) {{
{cases}
        default: return -1;
    }}
}}
"""


def _c_struct_alias(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    k1, k2 = rng.randrange(1, 100), rng.randrange(1, 100)
    return f"""/* generated deterministic structure/alias case */
typedef struct {fn}_record {{
    int x;
    short y;
    unsigned char flags;
    unsigned char pad;
    int values[4];
}} {fn}_record;

int {fn}({fn}_record *restrict out, const {fn}_record *restrict in) {{
    int total = in->x + (int)in->y + {k1};
    unsigned i;
    for (i = 0; i < 4; ++i) total += in->values[i] * (int)(i + {k2});
    out->x = total;
    out->flags = (unsigned char)(in->flags ^ {k1}u);
    return total;
}}
"""


def _c_bitfield(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    xor_value = rng.randrange(1, 31)
    return f"""/* generated deterministic bit-field case */
typedef struct {fn}_bits {{
    unsigned low : 5;
    unsigned mid : 11;
    unsigned high : 16;
}} {fn}_bits;

unsigned {fn}({fn}_bits *value, unsigned input) {{
    value->low = input & 31u;
    value->mid = (input >> 5) & 2047u;
    value->high = ((input >> 16) ^ {xor_value}u) & 65535u;
    return value->low + value->mid + value->high;
}}
"""


def _c_float(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    a = rng.randrange(1, 20) / 3.0
    b = rng.randrange(1, 20) / 7.0
    return f"""/* generated deterministic floating-point case */
double {fn}(double x, double y) {{
    double a = x * {a:.17g};
    double b = y + {b:.17g};
    return (a * b) - (x / (b + 1.0));
}}
"""


def _c_indirect(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    bias = rng.randrange(1, 100)
    return f"""/* generated deterministic indirect-call case */
typedef int (*{fn}_callback)(int, int);
int {fn}({fn}_callback callback, int x, int y) {{
    return callback(x + {bias}, y - {bias});
}}
"""


def _cpp_virtual(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    bias = rng.randrange(1, 100)
    return f"""// generated deterministic virtual-dispatch case
class {fn}_base {{
public:
    virtual ~{fn}_base() {{}}
    virtual int apply(int value) const = 0;
}};
class {fn}_derived final : public {fn}_base {{
    int bias_;
public:
    explicit {fn}_derived(int bias) : bias_(bias) {{}}
    int apply(int value) const override {{ return value * 3 + bias_; }}
}};
extern "C" int {fn}(int value) {{
    {fn}_derived object({bias});
    const {fn}_base &base = object;
    return base.apply(value);
}}
"""


def _cpp_multiple_inheritance(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    x, y = rng.randrange(1, 50), rng.randrange(1, 50)
    return f"""// generated deterministic multiple-inheritance case
struct {fn}_left {{ virtual ~{fn}_left() {{}}; virtual int left() const {{ return {x}; }}; }};
struct {fn}_right {{ virtual ~{fn}_right() {{}}; virtual int right() const {{ return {y}; }}; }};
struct {fn}_both final : {fn}_left, {fn}_right {{ int value; explicit {fn}_both(int v): value(v) {{}} }};
extern "C" int {fn}(int value) {{
    {fn}_both object(value);
    {fn}_left *left = &object;
    {fn}_right *right = &object;
    return left->left() + right->right() + object.value;
}}
"""


def _cpp_exception(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    marker = rng.randrange(2, 29)
    return f"""// generated deterministic exception case
struct {fn}_error {{ int code; }};
extern "C" int {fn}(int value) {{
    try {{
        if ((value % {marker}) == 0) throw {fn}_error{{value}};
        return value + {marker};
    }} catch (const {fn}_error &error) {{
        return -error.code;
    }}
}}
"""


def _cpp_template(case_id: str, rng: random.Random) -> str:
    fn = _symbol(case_id)
    value = rng.randrange(2, 64)
    return f"""// generated deterministic template-instantiation case
template <typename T, int Bias> static T {fn}_mix(T x, T y) {{ return x * y + (T)Bias; }}
extern "C" int {fn}(int x, int y) {{ return {fn}_mix<int, {value}>(x, y); }}
"""


_C_FAMILIES: dict[str, Callable[[str, random.Random], str]] = {
    "arithmetic": _c_arithmetic,
    "branches": _c_branches,
    "loop": _c_loop,
    "switch": _c_switch,
    "struct_alias": _c_struct_alias,
    "bitfield": _c_bitfield,
    "floating_point": _c_float,
    "indirect_call": _c_indirect,
}
_CPP_FAMILIES: dict[str, Callable[[str, random.Random], str]] = {
    "virtual_dispatch": _cpp_virtual,
    "multiple_inheritance": _cpp_multiple_inheritance,
    "exception": _cpp_exception,
    "template": _cpp_template,
}


def generate_synthetic_corpus(
    output_directory: Path,
    *,
    cases_per_family: int = 8,
    seed: int = 0x86DEC0DE,
    include_c: bool = True,
    include_cpp: bool = True,
    report_path: Path | None = None,
) -> dict[str, Any]:
    """Generate deterministic source cases and a compiler-corpus input manifest.

    The operation refuses a non-empty output directory to prevent accidental
    mixing of source corpora with different parameters.
    """
    if not isinstance(cases_per_family, int) or isinstance(cases_per_family, bool) or cases_per_family <= 0:
        raise ContractError("cases_per_family must be a positive integer")
    if cases_per_family > 10_000:
        raise ContractError("cases_per_family exceeds the bounded limit of 10000")
    if not include_c and not include_cpp:
        raise ContractError("at least one of include_c or include_cpp must be enabled")
    root = output_directory.resolve()
    if root.exists() and any(root.iterdir()):
        raise ContractError(f"synthetic corpus output directory is not empty: {root}")
    source_root = root / "sources"
    source_root.mkdir(parents=True, exist_ok=True)
    families: list[tuple[str, str, Callable[[str, random.Random], str]]] = []
    if include_c:
        families.extend(("c", name, generator) for name, generator in sorted(_C_FAMILIES.items()))
    if include_cpp:
        families.extend(("c++", name, generator) for name, generator in sorted(_CPP_FAMILIES.items()))
    cases: list[dict[str, Any]] = []
    ground_truth_cases: list[dict[str, Any]] = []
    for language, family, generator in families:
        for index in range(cases_per_family):
            case_seed = (seed ^ (len(cases) * 0x9E3779B1)) & 0xFFFFFFFFFFFFFFFF
            rng = random.Random(case_seed)
            case_id = f"generated_{family}_{index:05d}"
            suffix = ".c" if language == "c" else ".cpp"
            relative = Path("sources") / f"{case_id}{suffix}"
            source = root / relative
            source.write_text(generator(case_id, rng), encoding="utf-8", newline="\n")
            record = {
                "id": case_id,
                "family": family,
                "language": language,
                "seed": case_seed,
                "source": relative.as_posix(),
                "source_sha256": sha256_file(source),
                "generator": f"x86decomp.synthetic_corpus:{generator.__name__}",
            }
            cases.append(record)
            ground_truth_cases.append(
                {
                    "id": case_id,
                    "source": relative.as_posix(),
                    "language": language,
                    "arguments": ["-fexceptions", "-frtti"] if language == "c++" else [],
                }
            )
    report = {
        "schema_version": GENERATOR_SCHEMA_VERSION,
        "kind": "synthetic_source_corpus",
        "created_at": utc_now(),
        "seed": seed,
        "cases_per_family": cases_per_family,
        "families": [{"language": language, "name": name} for language, name, _ in families],
        "case_count": len(cases),
        "cases": cases,
        "truth_scope": {
            "source_generation_reproducible": True,
            "compiler_execution_performed": False,
            "binary_equivalence_claimed": False,
            "original_source_recovery_claimed": False,
        },
    }
    write_json(report_path or root / "corpus-generation.json", report)
    write_json(
        root / "ground-truth-cases.json",
        {
            "schema_version": 1,
            "kind": "ground_truth_case_fragment",
            "cases": ground_truth_cases,
            "note": "Add explicit compiler records and flag matrices before ground-truth-build.",
        },
    )
    return report


def verify_synthetic_corpus(report_path: Path) -> dict[str, Any]:
    report_file = report_path.resolve()
    report = __import__("json").loads(report_file.read_text(encoding="utf-8"))
    if report.get("schema_version") != GENERATOR_SCHEMA_VERSION or report.get("kind") != "synthetic_source_corpus":
        raise ContractError("not a supported synthetic source corpus report")
    root = report_file.parent
    failures: list[str] = []
    seen: set[str] = set()
    for record in report.get("cases", []):
        if not isinstance(record, dict):
            failures.append("case record is not an object")
            continue
        case_id = record.get("id")
        if not isinstance(case_id, str) or case_id in seen:
            failures.append(f"invalid or duplicate case id: {case_id!r}")
            continue
        seen.add(case_id)
        relative = Path(str(record.get("source", "")))
        if relative.is_absolute() or ".." in relative.parts:
            failures.append(f"unsafe source path: {relative}")
            continue
        source = (root / relative).resolve()
        try:
            source.relative_to(root)
        except ValueError:
            failures.append(f"source escapes corpus root: {relative}")
            continue
        if not source.is_file() or source.is_symlink():
            failures.append(f"source missing or unsafe: {relative}")
        elif sha256_file(source) != record.get("source_sha256"):
            failures.append(f"source hash mismatch: {relative}")
    expected = int(report.get("case_count", -1))
    if expected != len(seen):
        failures.append(f"case_count mismatch: declared {expected}, observed {len(seen)}")
    return {"valid": not failures, "case_count": len(seen), "failures": failures}
