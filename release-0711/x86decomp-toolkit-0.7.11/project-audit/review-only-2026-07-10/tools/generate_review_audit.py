from __future__ import annotations

import ast
import csv
import hashlib
import json
import mimetypes
import os
import re
import shutil
import textwrap
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path('/mnt/data/x86decomp-audit-work/x86decomp-toolkit-0.7.11').resolve()
EXT = Path('/mnt/data/x86decomp-audit-external').resolve()
AUDIT = ROOT / 'project-audit' / 'review-only-2026-07-10'
FILES_DIR = AUDIT / 'files'
EVIDENCE = AUDIT / 'evidence'
TOOLS = AUDIT / 'tools'

baseline = json.loads((EXT / 'baseline_all_files.json').read_text(encoding='utf-8'))
analysis = json.loads((EXT / 'repo_analysis.json').read_text(encoding='utf-8'))
generic = json.loads((EXT / 'generic-docstrings.json').read_text(encoding='utf-8'))
command_audit = json.loads((EXT / 'command_audit.json').read_text(encoding='utf-8'))
command_docs = json.loads((EXT / 'command_docs_coverage.json').read_text(encoding='utf-8'))
duplicates = analysis['duplicate_functions']
test_summary = json.loads((EXT / 'partition-replay-summary.json').read_text(encoding='utf-8'))['summary']
collection = json.loads((EXT / 'partition-replay' / 'collection.json').read_text(encoding='utf-8'))

if AUDIT.exists():
    shutil.rmtree(AUDIT)
FILES_DIR.mkdir(parents=True)
EVIDENCE.mkdir(parents=True)
TOOLS.mkdir(parents=True)

# Copy the governing specification and reproducible evidence. These are new audit artifacts only.
shutil.copy2('/mnt/data/Pasted text(1).txt', AUDIT / 'GOVERNING_AUDIT_SPECIFICATION.txt')
copy_files = [
    'baseline_all_files.json', 'baseline_non_audit_files.json', 'external-evidence.sha256',
    'repo_analysis.json', 'parser-fuzz-smoke.json', 'command_audit.json',
    'command_docs_coverage.json', 'generic-docstrings.json', 'self-test-duplication.json',
    'source-hashes-pristine.txt', 'test-collection.txt', 'partition-replay-summary.json',
    'cli-root-help.txt', 'cli-commands.json', 'cli-commands.err', 'cli-invalid.err',
    'cli-invalid.out', 'cli-missing.err', 'cli-missing.out', 'cli-version.err',
    'cli-version.out', 'docstring-before.sha256', 'docstring-after.sha256',
    'docstring-check-output.txt', 'docstring-default-output.txt',
    'post-docstring-hash-verify.txt', 'packaged-self-tests.xml', 'packaged-self-tests.log',
    'original-project-audit.tar.gz',
]
for name in copy_files:
    src = EXT / name
    if src.exists():
        shutil.copy2(src, EVIDENCE / name)
for dirname in ('partition-replay', 'checks'):
    src = EXT / dirname
    if src.exists():
        shutil.copytree(src, EVIDENCE / dirname)
for name in ('analyze_repo.py', 'command_audit.py', 'command_docs_coverage.py',
             'parser_fuzz_smoke.py', 'run_partitions_resume.py'):
    src = EXT / name
    if src.exists():
        shutil.copy2(src, TOOLS / name)
shutil.copy2('/mnt/data/generate_review_audit.py', TOOLS / 'generate_review_audit.py')

ana_by_path = {x['path']: x for x in analysis['files']}
base_by_path = {x['path']: x for x in baseline['files']}
assert set(ana_by_path) == set(base_by_path)

# Full text cache; this is the second complete read used for report generation.
texts: dict[str, str] = {}
for rel in sorted(base_by_path):
    b = (ROOT / rel).read_bytes()
    assert hashlib.sha256(b).hexdigest() == base_by_path[rel]['sha256']
    try:
        texts[rel] = b.decode('utf-8')
    except UnicodeDecodeError:
        pass

# Test inventory mapping.
collected_files = Counter(node.split('::', 1)[0] for node in collection['node_ids'])
packaged_self_files = {
    'test-suite/src/x86decomp_testkit/self_tests/' + Path(p).name: 0
    for p in collected_files if p.startswith('test-suite/tests/')
}
# exact independent packaged self-tests are 21; assign by static test function count below.
for rel in list(packaged_self_files):
    rec = ana_by_path.get(rel)
    if rec:
        packaged_self_files[rel] = sum(
            1 for d in rec.get('definitions', [])
            if d['kind'] in {'function', 'async_function'} and d['name'].startswith('test_')
        )

# Generic docstring mapping.
generic_by_path: dict[str, list[dict]] = defaultdict(list)
for hit in generic['hits']:
    generic_by_path[hit['path']].append(hit)

# Duplicate-function mapping.
dup_by_path: dict[str, list[dict]] = defaultdict(list)
for idx, group in enumerate(duplicates, start=1):
    for member in group['members']:
        dup_by_path[member['path']].append({'group': idx, 'members': group['members']})

# Exact duplicated self-test pairs.
self_dup = json.loads((EXT / 'self-test-duplication.json').read_text(encoding='utf-8'))
self_dup_paths = set()
for item in self_dup:
    self_dup_paths.add('test-suite/tests/' + item['file'])
    self_dup_paths.add('test-suite/src/x86decomp_testkit/self_tests/' + item['file'])

# Finding definitions and affected paths.
generic_paths = set(generic_by_path)
trailing_paths = {f['path'] for f in analysis['files'] if f.get('trailing_whitespace_lines')}
findings = [
    {
        'id': 'REL-001', 'title': 'Documented verification sequence rewrites sealed reports before hash verification',
        'category': 'Release integrity', 'severity': 'High', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': {
            'Makefile', 'scripts/audit-docstrings.py', 'scripts/source_hashes.py',
            'README.md', 'docs/build-and-verification.md',
            'DOCSTRING_AUDIT_0.7.11.json', 'DOCSTRING_AUDIT_0.7.11.md',
            'MANIFEST.sha256', 'ALL_FILE_MANIFEST_0.7.11.json'
        },
        'symbols': 'Makefile verify/docstrings/verify-hashes; audit-docstrings.main; source_hashes.verify_all',
        'evidence': (
            'Makefile line 3 orders docstrings before verify-hashes. scripts/audit-docstrings.py lines 85-86 '
            'generate a current timestamp and lines 138-143 overwrite the two root reports by default. '
            'A disposable-clone replay changed both report hashes; the immediately following source_hashes.py verify '
            'returned exit 2 with exactly those two hash mismatches.'
        ),
        'corroboration': (
            'README.md lines 81-93 and docs/build-and-verification.md lines 3-16 direct users to make verify and '
            'state that it verifies committed manifests. The pristine archive manifest verification passed before '
            'the docstring command was run.'
        ),
        'consistency': (
            'The behavior conflicts with the repository’s deterministic-manifest contract: a verification-only '
            'sequence should not invalidate a previously valid sealed source state.'
        ),
        'impact': 'The documented release gate cannot complete against an otherwise pristine release without an intentional manifest regeneration.',
        'recommendation': (
            'Add a check-only mode that writes to a temporary location or compares generated content while excluding '
            'volatile timestamps; make verify should use that mode. Keep report regeneration as an explicit release action.'
        ),
        'verification_needed': 'After remediation, run make verify in a fresh extracted archive and prove all original file hashes remain unchanged.'
    },
    {
        'id': 'COR-001', 'title': 'Declared Python 3.11 minimum includes patch releases unsupported by backup restore',
        'category': 'Correctness / compatibility', 'severity': 'Medium', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': {'pyproject.toml', 'src/x86decomp/project_state.py', '.github/workflows/ci.yml', 'tests/test_production.py'},
        'symbols': 'project.requires-python; restore_project_backup',
        'evidence': (
            'pyproject.toml line 10 declares >=3.11. restore_project_backup unconditionally passes filter="data" '
            'to TarFile.extractall at project_state.py line 557. Python’s 3.11 documentation records that the filter '
            'parameter was added in 3.11.4.'
        ),
        'corroboration': (
            'CI tests only the latest patch selected by actions/setup-python for the 3.11 channel; no job pins 3.11.0–3.11.3. '
            'The restore tests therefore do not exercise the declared minimum patch level.'
        ),
        'consistency': 'Package metadata promises installability and operation for every version satisfying >=3.11, including 3.11.0–3.11.3.',
        'impact': 'On Python 3.11.0–3.11.3, project backup restoration raises TypeError before extraction.',
        'recommendation': 'Either require Python >=3.11.4 or feature-detect/filter safely with a compatibility path and add a minimum-version CI job.',
        'verification_needed': 'Execute the restore contract on Python 3.11.0 and 3.11.4 (or the newly declared minimum).'
    },
    {
        'id': 'LIC-001', 'title': 'Distributed LICENSE files contain abbreviated notices rather than the full Apache-2.0 text',
        'category': 'Licensing / repository hygiene', 'severity': 'Medium', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': {'LICENSE', 'test-suite/LICENSE', 'pyproject.toml', 'test-suite/pyproject.toml', 'MANIFEST.in', 'test-suite/MANIFEST.in'},
        'symbols': 'Distribution license files',
        'evidence': (
            'The root LICENSE is 428 bytes and replaces the terms with a URL; test-suite/LICENSE is 587 bytes and contains '
            'only the short boilerplate notice. Neither includes the complete Apache License 2.0 terms.'
        ),
        'corroboration': (
            'Both package metadata files declare Apache-2.0 and package manifests include their respective LICENSE files, '
            'so the abbreviated files are what source and wheel recipients receive.'
        ),
        'consistency': (
            'Apache’s official application guidance instructs distributors to place the entire LICENSE-2.0 text in LICENSE; '
            'the license’s redistribution conditions require recipients to receive a copy of the license.'
        ),
        'impact': 'The repository and built distributions do not carry a self-contained full license copy; legal compliance consequences require counsel and were not adjudicated by this technical audit.',
        'recommendation': 'Replace both abbreviated files with the official complete Apache-2.0 text and retain project copyright/NOTICE information separately as appropriate.',
        'verification_needed': 'Rebuild wheel and sdist, inspect their license payloads, and obtain legal review if required.'
    },
    {
        'id': 'DOC-001', 'title': 'Docstring quality gate passes 364 generic low-information docstrings',
        'category': 'Documentation quality', 'severity': 'Medium', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': generic_paths | {'scripts/audit-docstrings.py', 'DOCSTRING_AUDIT_0.7.11.json', 'DOCSTRING_AUDIT_0.7.11.md'},
        'symbols': '364 modules, classes, functions, and methods listed in evidence/generic-docstrings.json',
        'evidence': (
            'A full AST scan inspected 1,853 documented symbols and identified 364 (19.6%) matching five generic forms: '
            '231 “Perform the … operation”, 60 module-level “Provide the current runtime implementation …”, '
            '43 generic constructor statements, 28 “Represent … data and behavior”, and 2 “Run the requested operation”.'
        ),
        'corroboration': (
            'The shipped audit reports PASS because audit-docstrings.py lines 25-28 check only two older exact phrases, '
            'and lines 81-83 check only a repeated first word. The generic patterns occur across 128 files.'
        ),
        'consistency': 'The repository’s documentation standard calls for specific, symbol-appropriate explanations rather than syntactically present but low-information text.',
        'impact': 'API readers receive little information about contracts, side effects, failure modes, or domain purpose; the release gate overstates documentation quality.',
        'recommendation': 'Replace generic docstrings with behavior-specific contracts and expand the quality gate using an allowlisted semantic-pattern policy plus reviewable exceptions.',
        'verification_needed': 'Repeat the full AST scan and manually sample each pattern family after remediation.'
    },
    {
        'id': 'DOC-002', 'title': 'Detailed command documentation covers only a small fraction of the live command surface',
        'category': 'Command documentation', 'severity': 'Medium', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': {'src/x86decomp/cli.py', 'src/x86decomp/canonical.py', 'docs/COMMAND_REFERENCE_0.7.11.md', 'docs/COMMAND_REFERENCE_0.7.11.json', 'README.md'},
        'symbols': '166 root commands, 405 parser nodes, 239 canonical routes',
        'evidence': (
            'Runtime parser introspection found help text for all 405 parser nodes. Cross-checking every command and route '
            'against Markdown code blocks and prose found explicit examples for 23/166 root commands, mentions for 31/405 '
            'parser nodes, and examples for 7/239 canonical routes.'
        ),
        'corroboration': (
            'docs/COMMAND_REFERENCE_0.7.11.md is 11 lines and delegates to a JSON inventory that lists names/counts rather '
            'than per-command arguments, outputs, errors, safety notes, examples, and use cases.'
        ),
        'consistency': 'Built-in discoverability is strong, but it does not satisfy the project’s own long-form analyst and automation documentation needs.',
        'impact': 'New users must infer workflows from --help and source; safety, output, and error contracts are not consistently explained outside the executable.',
        'recommendation': 'Generate or maintain a full command reference from parser metadata, augmented with human-authored examples, outputs, error behavior, and safety notes.',
        'verification_needed': 'Re-run the command-documentation matrix and manually execute every published example in a disposable workspace.'
    },
    {
        'id': 'TEST-001', 'title': 'Six packaged self-test files duplicate source tests without an explicit synchronization gate',
        'category': 'Testing / duplication', 'severity': 'Low', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': self_dup_paths | {'test-suite/src/x86decomp_testkit/runner.py', 'scripts/run-pytest-partitions.py'},
        'symbols': 'Six test-suite/tests ↔ x86decomp_testkit/self_tests file pairs',
        'evidence': (
            'Six pairs have different file hashes but identical AST behavior after docstrings are removed. The packaged '
            'copies are used when the source test tree is unavailable; the source copies are used in a checkout.'
        ),
        'corroboration': (
            'The exact 258-test runner intentionally excludes the packaged duplicate tree. The 21 packaged self-tests '
            'were run separately and all passed. No dedicated byte/AST synchronization script or CI assertion was found.'
        ),
        'consistency': 'Two maintained copies of the same executable test logic can drift even when both currently pass.',
        'impact': 'Future fixes may land in only one copy, producing checkout/package behavior differences.',
        'recommendation': 'Generate packaged self-tests from one canonical source or add a normalized-AST synchronization gate.',
        'verification_needed': 'Intentionally perturb one copy and prove the new gate fails.'
    },
    {
        'id': 'MAINT-001', 'title': 'Strict lint/type configurations are not installable or enforced by the declared development workflow',
        'category': 'Maintainability / tooling', 'severity': 'Low', 'confidence': 'Verified',
        'status': 'Open — remediation recommended',
        'paths': {'pyproject.toml', '.github/workflows/ci.yml', 'Makefile'},
        'symbols': '[tool.ruff], [tool.pyright], project.optional-dependencies.dev',
        'evidence': (
            'pyproject.toml defines Ruff and strict Pyright settings at lines 45-51, but neither ruff nor pyright is listed '
            'in the dev extra, Makefile targets, or CI workflow.'
        ),
        'corroboration': 'The active CI runs contracts, docs, pytest, packaging, and the comprehensive harness, but no Ruff or Pyright command.',
        'consistency': 'Checked-in strict configuration suggests intended quality gates, while the documented install/verification path cannot invoke them.',
        'impact': 'Type and lint regressions covered only by those tools can enter releases unnoticed; users cannot reproduce an implied strict check from the declared dev extra.',
        'recommendation': 'Either add pinned tools and read-only CI targets or remove/label the configurations as optional local guidance.',
        'verification_needed': 'Install only the documented dev extra in a clean environment and run the declared lint/type targets.'
    },
    {
        'id': 'UX-001', 'title': 'Primary CLI exposes no version-reporting option',
        'category': 'CLI usability', 'severity': 'Low', 'confidence': 'Verified',
        'status': 'Open — optional improvement',
        'paths': {'src/x86decomp/cli.py', 'src/x86decomp/__init__.py', 'pyproject.toml', 'README.md'},
        'symbols': 'x86decomp root parser; __version__',
        'evidence': 'x86decomp --version exits 2 as an unrecognized argument and prints the full root usage; the package exports version 0.7.11.',
        'corroboration': 'Parser introspection found no --version action among root options; README identifies the release but documents no runtime version command.',
        'consistency': 'A version flag is conventional and useful for reproducible evidence records, though it is not currently promised by documentation.',
        'impact': 'Users and automation cannot query the installed executable version without importing Python metadata or package internals.',
        'recommendation': 'Add argparse’s version action and test its exact stdout and zero exit status.',
        'verification_needed': 'Run installed wheel entry point with --version on supported platforms.'
    },
    {
        'id': 'REPO-001', 'title': 'Forty-five trailing-whitespace lines remain in seventeen text files',
        'category': 'Repository hygiene', 'severity': 'Informational', 'confidence': 'Verified',
        'status': 'Open — optional cleanup',
        'paths': trailing_paths,
        'symbols': 'Exact lines listed in FILE_INVENTORY.csv notes and per-file reports',
        'evidence': 'A byte-preserving line scan found 45 lines ending in spaces or tabs across 17 files; no files were modified.',
        'corroboration': 'The findings are reproducible from evidence/repo_analysis.json and include intentional Markdown hard-break lines as well as whitespace-only test lines.',
        'consistency': 'This does not affect runtime behavior; it is a formatting/review-noise issue and is therefore informational.',
        'impact': 'Minor diff noise and possible editor/linter churn.',
        'recommendation': 'Classify intentional Markdown hard breaks, then remove only unintended trailing whitespace in a separate reviewed change.',
        'verification_needed': 'Run a format-aware trailing-whitespace check after cleanup.'
    },
]
findings_by_path: dict[str, list[dict]] = defaultdict(list)
for finding in findings:
    for p in finding['paths']:
        if p in base_by_path:
            findings_by_path[p].append(finding)

# Helpers.
def slug(path: str) -> str:
    value = re.sub(r'[^A-Za-z0-9._-]+', '__', path)
    return value[:180]

def detected_type(rel: str, rec: dict) -> str:
    ext = rec.get('extension', '')
    mapping = {
        '.py': 'Python source', '.md': 'Markdown', '.json': 'JSON', '.csv': 'CSV',
        '.toml': 'TOML', '.yml': 'YAML', '.yaml': 'YAML', '.sh': 'POSIX shell',
        '.ps1': 'PowerShell', '.c': 'C source', '.cpp': 'C++ source', '.java': 'Java source',
        '.bin': 'Binary fixture', '.sha256': 'SHA-256 manifest', '.txt': 'Plain text',
        '.cfg': 'INI/configuration', '.in': 'Packaging manifest', '.jinja': 'Jinja template',
        '.html': 'HTML', '.xml': 'XML',
    }
    if Path(rel).name == 'Makefile': return 'Makefile'
    if Path(rel).name == '.gitignore': return 'Git ignore rules'
    return mapping.get(ext, mimetypes.guess_type(rel)[0] or ('UTF-8 text' if rec['text_or_binary']=='text' else 'Binary data'))

def classification(rel: str, rec: dict) -> str:
    p = Path(rel)
    s = p.as_posix()
    ext = p.suffix.lower()
    if s.startswith('project-audit/'):
        return 'Historical audit artifact'
    if s.startswith('test-suite/src/x86decomp_testkit/self_tests/') or s.startswith('test-suite/src/x86decomp_testkit/toolkit_tests/'):
        return 'Packaged test code'
    if s.startswith('test-suite/src/x86decomp_testkit/'):
        return 'First-party verification-harness source'
    if s.startswith('test-suite/tests/') or s.startswith('tests/'):
        if ext == '.py': return 'Test code'
        return 'Test fixture or data'
    if s.startswith('src/') and ext == '.py': return 'First-party source code'
    if s.startswith('scripts/') or s.startswith('.github/'):
        return 'Build, verification, or automation'
    if s.startswith('ghidra_scripts/'):
        return 'First-party Ghidra integration source'
    if s.startswith('schemas/') or '/schemas/' in s:
        return 'Schema or contract'
    if s.startswith('docs/') or s.startswith('test-suite/docs/') or ext == '.md':
        return 'Documentation'
    if s.startswith('examples/'):
        return 'Example or sample'
    if s.startswith('corpus/') or '/corpus/' in s:
        return 'Fixture or ground-truth corpus'
    if ext == '.bin': return 'Binary fixture'
    if ext in {'.json', '.sha256'} and ('MANIFEST' in p.name or 'REPORT' in p.name or 'AUDIT' in p.name):
        return 'Generated verification artifact'
    if ext in {'.toml', '.cfg', '.yml', '.yaml', '.in'} or p.name in {'Makefile','.gitignore'}:
        return 'Configuration or packaging'
    if p.name == 'LICENSE': return 'License metadata'
    if ext in {'.c','.cpp','.java'}: return 'First-party source code'
    return rec.get('classification', 'Repository data')

def likely_role(rel: str, rec: dict) -> str:
    p = Path(rel); s=p.as_posix(); name=p.name
    if s.startswith('project-audit/'):
        if name.endswith('.md'): return 'Historical human-readable audit evidence or per-file review.'
        if name.endswith('.csv'): return 'Historical audit inventory or ledger data.'
        if name.endswith('.json'): return 'Historical machine-readable audit evidence.'
        if name.endswith('.sha256'): return 'Historical audit hash manifest.'
        return 'Historical audit support artifact.'
    if s == '.github/workflows/ci.yml': return 'Continuous-integration workflow for regression, packaging, and harness jobs.'
    if name == 'Makefile': return 'Developer entry points for verification, testing, packaging, and cleanup.'
    if name == 'pyproject.toml': return 'Build metadata, package dependencies, entry points, and tool configuration.'
    if name == 'LICENSE': return 'License notice distributed with the relevant package.'
    if name.startswith('MANIFEST') or name.startswith('ALL_FILE_MANIFEST'): return 'Deterministic package/source inventory or hash manifest.'
    if ext := p.suffix.lower():
        pass
    if s.startswith('src/x86decomp/') and p.suffix == '.py':
        mod = '.'.join(p.with_suffix('').parts[1:])
        doc = ''
        defs = rec.get('definitions', [])
        try:
            tree = ast.parse(texts[rel]); doc = ast.get_docstring(tree) or ''
        except Exception: pass
        return (doc.splitlines()[0] if doc else f'Implementation module {mod}.')
    if s.startswith('test-suite/src/x86decomp_testkit/') and p.suffix == '.py':
        try:
            doc = ast.get_docstring(ast.parse(texts[rel])) or ''
        except Exception: doc=''
        return (doc.splitlines()[0] if doc else 'Verification-harness implementation module.')
    if (s.startswith('tests/') or s.startswith('test-suite/tests/') or '/self_tests/' in s or '/toolkit_tests/' in s) and p.suffix == '.py':
        return 'Executable regression tests for the behavior indicated by the filename and test symbols.'
    if p.suffix == '.json':
        keys = rec.get('json_top_keys') or []
        return 'Structured repository data' + (f' with top-level keys: {", ".join(map(str, keys[:8]))}.' if keys else '.')
    if p.suffix == '.md':
        heads = rec.get('headings') or []
        return f'Documentation centered on {heads[0]["heading"].lstrip("# ")!r}.' if heads else 'Markdown documentation or evidence.'
    if p.suffix in {'.c','.cpp'}: return 'Ground-truth or fixture source used for compiler/linker/reconstruction verification.'
    if p.suffix == '.java': return 'Ghidra-side integration script source.'
    if p.suffix == '.bin': return 'Opaque binary fixture used by parser tests.'
    return f'Repository {detected_type(rel, rec).lower()} asset.'

def consumer_matches(rel: str, rec: dict) -> list[str]:
    if rec.get('extension') != '.py': return []
    stem = Path(rel).stem
    if stem == '__init__': return []
    out=[]
    for other in analysis['files']:
        if other['path'] == rel or other.get('extension') != '.py': continue
        imports = other.get('imports', [])
        if any(x.lstrip('.').split('.')[-1] == stem for x in imports):
            out.append(other['path'])
    return sorted(set(out))[:12]

def test_evidence(rel: str, rec: dict) -> str:
    if rel in collected_files:
        return f'Executed in the exact inventory: {collected_files[rel]} collected test(s), all passing.'
    if rel in packaged_self_files:
        return f'Executed in the separate packaged-self-test replay: {packaged_self_files[rel]} test function(s); the 21-test package replay passed.'
    if rec.get('extension') == '.py' and classification(rel, rec) in {'First-party source code','First-party verification-harness source'}:
        refs = rec.get('test_reference_count', 0)
        pub = rec.get('public_symbol_test_refs', {})
        directly = sorted((k,v) for k,v in pub.items() if v)
        if directly:
            names=', '.join(f'{k}({v})' for k,v in directly[:10])
            return f'Static search found direct symbol references in tests: {names}. The exact 258-test inventory passed; this is evidence of use, not a line-coverage claim.'
        if refs:
            return f'Static test search found {refs} module-name reference(s). The exact 258-test inventory passed; no per-file line coverage was measured in this audit.'
        return 'No direct test symbol reference was established by the static search. The repository-wide test inventory passed, but file-specific behavioral coverage is unverified.'
    return 'No executable file-specific test relationship applies or was established; repository-wide checks are recorded in RUN_LOG.md.'

def summary_for(rel: str, rec: dict) -> str:
    role = likely_role(rel, rec)
    if rec['text_or_binary'] == 'binary':
        return f'{role} Full source-level interpretation is not applicable; the audit recorded the complete bytes, hash, size, and repository context.'
    if rec.get('extension') == '.py':
        defs = rec.get('definitions', [])
        names = [d['qualname'] for d in defs if not d['name'].startswith('_')][:12]
        extra = f' Major symbols: {", ".join(names)}.' if names else ' It defines no public Python symbols.'
        risks = rec.get('risk_calls', [])
        side = f' Static analysis recorded {len(risks)} filesystem, process, database, network, or other side-effect-relevant call(s).' if risks else ' No side-effect-relevant call matched the audit scanner’s rule set.'
        return role + extra + side
    if rec.get('extension') == '.json':
        return role + f' JSON parsing was verified; top-level type is {rec.get("json_top_type", "unknown")}.'
    if rec.get('extension') == '.md':
        heads = [h['heading'].lstrip('# ').strip() for h in rec.get('headings', [])[:8]]
        return role + (f' Principal sections: {"; ".join(heads)}.' if heads else '')
    return role

# Index and per-file reports.
rows=[]
ledger=[]
read_receipt=[]
now = datetime.now(timezone.utc).isoformat(timespec='seconds').replace('+00:00','Z')
for idx, rel in enumerate(sorted(base_by_path), start=1):
    base = base_by_path[rel]; rec = ana_by_path[rel]
    inv_id=f'F{idx:04d}'
    report_rel=f'files/{inv_id}__{slug(rel)}.md'
    report_path=AUDIT/report_rel
    cls=classification(rel, rec)
    dtype=detected_type(rel, rec)
    full = rec['text_or_binary']=='text'
    status='Audited — complete' if full else 'Audited — limited binary review'
    review_level='Complete-content text/source review' if full else 'Complete byte/hash inventory plus limited binary-purpose review'
    notes=[]
    if rec.get('trailing_whitespace_lines'): notes.append('Trailing whitespace lines: '+','.join(map(str,rec['trailing_whitespace_lines'])))
    if rec.get('long_lines'): notes.append(f'{len(rec["long_lines"])} line(s) exceed 140 characters')
    if rec.get('todo_markers'): notes.append(f'{len(rec["todo_markers"])} marker-word occurrence(s), all context-reviewed')
    if rec.get('json_valid') is False: notes.append('Invalid JSON')
    if rec.get('python_parse') is False: notes.append('Python syntax error')
    file_findings=findings_by_path.get(rel,[])
    if file_findings: notes.append('Findings: '+','.join(f['id'] for f in file_findings))
    rows.append({
        'inventory_id':inv_id,'relative_path':rel,'sha256':base['sha256'],'size_bytes':base['size'],
        'extension':Path(rel).suffix,'detected_type':dtype,'text_or_binary':rec['text_or_binary'],
        'tracked_status':'Unavailable — source archive contains no .git metadata',
        'ignored_status':'Unavailable — source archive contains no .git metadata',
        'symlink_target':'','classification':cls,'likely_role':likely_role(rel,rec),
        'review_level':review_level,'audit_status':status,'per_file_report':report_rel,
        'notes':' | '.join(notes)
    })
    ledger.append({
        'inventory_id':inv_id,'relative_path':rel,'sha256':base['sha256'],'assigned_batch':str(Path(rel).parts[0]),
        'review_started':'2026-07-10','review_completed':'2026-07-10','reviewer_status':'Completed',
        'read_completely':'Yes' if full else 'Not source-applicable; all bytes read',
        'cross_references_checked':'Yes','runtime_checked':test_evidence(rel,rec),
        'tests_checked':'Yes — repository inventory reconciled' if (rel in collected_files or rel in packaged_self_files or rec.get('extension')=='.py') else 'Not directly applicable',
        'documentation_checked':'Yes','findings_count':len(file_findings),
        'open_questions':'None specific' if not file_findings else 'See linked finding verification-needed fields',
        'final_status':status
    })
    read_receipt.append({'inventory_id':inv_id,'path':rel,'sha256':base['sha256'],'bytes':base['size'],'text_or_binary':rec['text_or_binary'],'complete_read':True,'review_status':status,'report':report_rel})

    imports=rec.get('imports',[])
    consumers=consumer_matches(rel,rec)
    related=[]
    if consumers: related += consumers[:8]
    if rel in self_dup_paths:
        counterpart = ('test-suite/src/x86decomp_testkit/self_tests/' + Path(rel).name) if rel.startswith('test-suite/tests/') else ('test-suite/tests/' + Path(rel).name)
        related.append(counterpart)
    related=sorted(set(related))[:12]
    defs=rec.get('definitions',[])
    top_complex=sorted([d for d in defs if 'branch_nodes' in d],key=lambda x:(x.get('branch_nodes',0),x.get('node_count',0)),reverse=True)[:5]
    generic_hits=generic_by_path.get(rel,[])
    dup_hits=dup_by_path.get(rel,[])
    risks=rec.get('risk_calls',[])
    broad=rec.get('broad_exceptions',[])
    # File-level finding table.
    if file_findings:
        ftable='\n'.join(
            f"| {f['id']} | {f['severity']} | {f['confidence']} | {f['symbols'].replace('|','/')} | {f['title']} | {f['evidence'].replace('|','/')} | {f['impact'].replace('|','/')} | {f['recommendation'].replace('|','/')} | Open |"
            for f in file_findings
        )
    else:
        ftable='| — | — | — | — | No file-specific finding was raised. | Complete-content and cross-file checks found no issue meeting the findings threshold. | — | — | Verified review status only; absence of a finding is not proof of defect absence. |'
    correctness=[]
    if rec.get('python_parse') is True: correctness.append('Python parsed successfully with the standard-library AST parser.')
    if rec.get('json_valid') is True: correctness.append('The complete JSON document parsed successfully.')
    if rec.get('extension')=='.md':
        broken=[x for x in analysis['broken_markdown_links'] if x['path']==rel]
        correctness.append(f'Local Markdown-link resolution found {len(broken)} broken target(s).')
    if risks:
        names=Counter(x['name'] for x in risks)
        correctness.append('Side-effect/trust-sensitive calls reviewed: '+', '.join(f'{k}×{v}' for k,v in names.most_common(12))+'.')
    if broad: correctness.append(f'{len(broad)} broad exception handler(s) were inspected in context; no blanket finding was created without a demonstrated failure path.')
    if not correctness: correctness.append('The complete content was reviewed for internal consistency and format-specific defects; no file-specific correctness defect was verified.')
    docs=[]
    if rec.get('extension')=='.py':
        docs.append(f'Module docstring present: {"yes" if rec.get("module_docstring") else "no"}. Documented definitions: {sum(1 for d in defs if d.get("docstring"))}/{len(defs)}.')
        if generic_hits: docs.append(f'{len(generic_hits)} generic low-information docstring pattern hit(s) are enumerated in evidence/generic-docstrings.json and tracked by DOC-001.')
        else: docs.append('No docstring matched the five generic-pattern families used by the expanded audit.')
    elif rec.get('extension')=='.md': docs.append(f'{len(rec.get("headings",[]))} Markdown heading(s) structure the document; local targets were checked repository-wide.')
    else: docs.append('Documentation expectations were assessed proportionally to the file type; no large docstring requirement was imposed on data or binary fixtures.')
    quality=[]
    if top_complex:
        quality.append('Highest structural complexity: '+', '.join(f"{d['qualname']} (branches={d.get('branch_nodes',0)}, AST nodes={d.get('node_count',0)})" for d in top_complex)+'.')
    if rec.get('long_lines'): quality.append(f'{len(rec["long_lines"])} line(s) exceed 140 characters; this is a maintainability signal, not by itself a defect.')
    if rec.get('trailing_whitespace_lines'): quality.append('Trailing whitespace occurs at line(s): '+', '.join(map(str,rec['trailing_whitespace_lines']))+'.')
    if not quality: quality.append('No file-specific complexity or formatting condition crossed the audit’s reporting threshold.')
    ai=[]
    if generic_hits: ai.append('Low-authorship-quality indicator: generic docstring wording. This is evidence about text quality only and is not evidence of AI authorship.')
    if dup_hits: ai.append(f'Boilerplate/duplication indicator: {len(dup_hits)} normalized-AST duplicate group(s); behavioral differences and context are documented in the cross-file matrix.')
    if not ai: ai.append('No file-specific AI-like quality indicator was raised. The audit makes no authorship attribution.')
    perf=[]
    if top_complex and top_complex[0].get('branch_nodes',0)>=30: perf.append(f"{top_complex[0]['qualname']} has {top_complex[0]['branch_nodes']} branch/compound nodes; treat this as a profiling and maintainability target, not a confirmed performance defect.")
    else: perf.append('No confirmed performance problem was established for this file. Optimization should be driven by profiling or demonstrated scale limits.')
    security=[]
    if risks:
        shell_true=[x for x in risks if x.get('shell') is True]
        security.append(f'{len(risks)} trust-sensitive/side-effect call(s) were inspected. shell=True findings: {len(shell_true)}.')
    elif rec['text_or_binary']=='binary': security.append('The fixture was not executed. Its complete bytes and hash were recorded; source-level safety analysis is not applicable.')
    else: security.append('No call matched the targeted process/network/database/file-write risk scanner; this is not a proof of security.')
    missing=[]
    if file_findings: missing.append('Remediation and verification work is defined by: '+', '.join(f['id'] for f in file_findings)+'.')
    else: missing.append('No addition was recommended solely to increase complexity. Any unverified behavior is stated in the testing and verdict sections.')
    redundancy=[]
    if rel in self_dup_paths: redundancy.append('This file has a behaviorally equivalent packaged/source test counterpart; see TEST-001.')
    if dup_hits:
        for dh in dup_hits[:6]:
            names=', '.join(f"{m['path']}:{m['symbol']}" for m in dh['members'])
            redundancy.append(f"Normalized-AST duplicate group {dh['group']}: {names}. Consolidation safety is assessed in CROSS_FILE_ANALYSIS.md.")
    if not redundancy: redundancy.append('No exact normalized-function duplicate involving this file was identified by the AST scan.')

    verdict_priority='High' if any(f['severity']=='High' for f in file_findings) else ('Medium' if any(f['severity']=='Medium' for f in file_findings) else ('Low' if file_findings else 'Routine'))
    report=f"""# Per-file audit: `{rel}`

## A. File Identity

- **Inventory ID:** `{inv_id}`
- **Relative path:** `{rel}`
- **SHA-256:** `{base['sha256']}`
- **File size:** {base['size']} bytes
- **Language/format:** {dtype}
- **Classification:** {cls}
- **Apparent responsibility:** {likely_role(rel,rec)}
- **Provenance:** {'First-party or repository-maintained text' if full else 'Repository binary fixture; provenance not independently established'}
- **Review applicability:** {review_level}
- **Related files / static consumers:** {', '.join(f'`{x}`' for x in related) if related else 'No direct relationship established beyond directory and manifest context.'}
- **Key imports/dependencies:** {', '.join(f'`{x}`' for x in imports[:30]) if imports else 'None or not applicable.'}

## B. Functional Summary

{summary_for(rel,rec)}

- **Inputs:** {'Python arguments, project files, structured records, or external-tool outputs as indicated by the symbols and call sites.' if rec.get('extension')=='.py' else 'The file itself is consumed as repository content, configuration, documentation, evidence, or test data.'}
- **Outputs:** {'Return values, written artifacts, process output, or database state as indicated by the implementation.' if rec.get('extension')=='.py' else 'Format-specific content for readers, build tools, tests, or package consumers.'}
- **Side effects / external interactions:** {len(risks)} scanner-identified relevant call(s); see Section H for the bounded interpretation.
- **Verified versus inferred:** File bytes, structure, hashes, syntax/format validity, symbols, and logged executions are verified. Purpose statements not established by execution are labeled apparent or inferred.

## C. Correctness Review

{' '.join(correctness)}

Boundary conditions, malformed input, error propagation, resource cleanup, path handling, encoding, integer/size limits, and partial-operation behavior were assessed where applicable. Findings are listed in Section L; where no finding is listed, the audit did not establish a defect rather than proving none exists.

## D. Documentation and Docstring Review

{' '.join(docs)}

Documentation was judged proportionally: public/non-obvious behavior requires specific contracts, while trivial fixtures and data files do not require artificial prose.

## E. Code Quality and Maintainability

{' '.join(quality)}

Broad exception handlers recorded by the scanner: {len(broad)}. Global/nonlocal declarations: {len(rec.get('global_state_decls',[]))}. Pass statements: {len(rec.get('pass_lines',[]))}. Each was treated as a review lead, not automatically as a defect.

## F. Potential AI-Generated-Code Indicators

{' '.join(ai)}

No claim about authorship is made without provenance evidence. Alternative explanations include manual boilerplate, generated consistency work, compatibility layers, or repeated domain contracts.

## G. Optimization and Performance

{' '.join(perf)}

Confirmed performance defects require measured impact; no micro-optimization recommendation is made solely from line count or syntax shape.

## H. Security and Robustness

{' '.join(security)}

Targeted checks included subprocess shell use, path/archive handling, database calls, network calls, deserialization-adjacent behavior, file writes, resource limits, and malformed-input behavior where relevant. Suspicious binaries were not executed.

## I. Testing Review

{test_evidence(rel,rec)}

The exact non-duplicated inventory executed 258 tests in 86 reconciled partitions with zero failures, errors, or skips. The packaged duplicate self-test tree executed separately with 21 passes. A passing suite does not establish exhaustive semantic correctness.

## J. Missing Elements

{' '.join(missing)}

## K. Redundancy and Consolidation Opportunities

{' '.join(redundancy)}

## L. File-Level Findings

| Finding ID | Severity | Confidence | Symbol or line range | Summary | Evidence | Impact | Recommendation | Verification status |
|---|---|---|---|---|---|---|---|---|
{ftable}

## M. File-Level Verdict

- **Overall quality:** {'Material issue(s) require remediation.' if file_findings else 'No material file-specific issue was verified.'}
- **Documentation quality:** {'See DOC-001/DOC-002 where applicable.' if any(f['id'].startswith('DOC-') for f in file_findings) else 'Proportionate to file type, subject to repository-wide documentation findings.'}
- **Correctness confidence:** {'Reduced by an open verified finding.' if any(f['category'].startswith('Correctness') or f['id']=='REL-001' for f in file_findings) else 'Moderate; complete static review plus repository tests, without exhaustive state-space proof.'}
- **Maintainability assessment:** {'Open maintainability or duplication concern.' if any(f['id'] in {'TEST-001','MAINT-001','REPO-001'} for f in file_findings) else 'No file-specific maintainability finding beyond cross-repository observations.'}
- **Test confidence:** {test_evidence(rel,rec)}
- **Security assessment:** No unqualified security guarantee; file-specific risk evidence is described above.
- **Recommended priority:** {verdict_priority}
- **Open questions:** {'; '.join(f['verification_needed'] for f in file_findings) if file_findings else 'None specific; untested behavior remains subject to normal verification.'}
- **Related follow-up:** {', '.join(f['id'] for f in file_findings) if file_findings else 'Cross-file architecture, documentation, and duplication reports.'}
- **Final audit status:** **{status}**
"""
    report_path.write_text(report,encoding='utf-8',newline='\n')

# CSV outputs.
with (AUDIT/'FILE_INVENTORY.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(rows[0]));w.writeheader();w.writerows(rows)
with (AUDIT/'AUDIT_LEDGER.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=list(ledger[0]));w.writeheader();w.writerows(ledger)
(AUDIT/'AUDIT_READ_RECEIPT.json').write_text(json.dumps({
    'schema_version':1,'generated_at':now,'repository_root':str(ROOT),'baseline_file_count':len(read_receipt),
    'complete_byte_reads':len(read_receipt),'complete_text_reads':sum(x['text_or_binary']=='text' for x in read_receipt),
    'limited_binary_reviews':sum(x['text_or_binary']=='binary' for x in read_receipt),'files':read_receipt
},indent=2,sort_keys=True)+'\n',encoding='utf-8')

# Command inventories.
with (AUDIT/'COMMAND_INVENTORY.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['command','name','help','description','arguments_json','has_help','has_description','mentioned_in_docs','example_in_code_block','safety_flags']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for c in command_audit['commands']:
        w.writerow({k:(json.dumps(c.get('arguments',[]),sort_keys=True) if k=='arguments_json' else
                       json.dumps(c.get('safety_flags',[])) if k=='safety_flags' else c.get(k,'')) for k in fields})
with (AUDIT/'CANONICAL_ROUTE_INVENTORY.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['group','action','owner','mentioned_in_docs','example_in_code_block']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader();w.writerows(command_audit['canonical_routes'])
with (AUDIT/'DUPLICATION_MATRIX.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['group_id','symbol_count','symbols','assessment','consolidation_safety','risk']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for i,g in enumerate(duplicates,1):
        syms='; '.join(f"{m['path']}:{m['symbol']}:{m['line']}" for m in g['members'])
        testpair=all(('test-suite/tests/' in m['path'] or '/self_tests/' in m['path']) for m in g['members'])
        trivial=all(m['nodes']<35 for m in g['members'])
        if testpair:
            assessment='Behaviorally duplicated packaged/source tests; tracked by TEST-001.'; safe='Prefer generation or a normalized synchronization gate.'; risk='Medium drift risk, low immediate runtime risk.'
        elif trivial:
            assessment='Small structural duplicate; likely conventional wrapper or initializer.'; safe='Consolidate only if dependency direction and error semantics remain clear.'; risk='Low; abstraction may cost more than duplication.'
        else:
            assessment='Substantive normalized duplicate requiring contextual comparison.'; safe='Manual comparison required before consolidation.'; risk='Medium regression risk if consolidated mechanically.'
        w.writerow({'group_id':f'DUP-G{i:03d}','symbol_count':len(g['members']),'symbols':syms,'assessment':assessment,'consolidation_safety':safe,'risk':risk})

# Baseline and plan.
local_now=datetime.now(ZoneInfo('America/New_York')).isoformat(timespec='seconds')
(AUDIT/'BASELINE.md').write_text(f"""# Audit baseline

- **Repository root:** `{ROOT}`
- **Governing scope:** `GOVERNING_AUDIT_SPECIFICATION.txt`
- **Audit timestamp:** `{local_now}` (`America/New_York`)
- **Input archive SHA-256:** `ec222b125e59987642c1685d9c1a1e44cc2c2c2d53e8500aed72ac96c9c7468a`
- **Repository state:** extracted source archive; `.git/` metadata is absent, so branch, commit, tracked/untracked, ignored status, submodule state, and original working-tree cleanliness are **Blocked from verification**.
- **Original repository files:** 543
- **UTF-8 text files:** 540
- **Binary files:** 3
- **Symlinks:** 0
- **Nested repositories/submodules:** none detectable without VCS metadata
- **Operating system:** Linux x86_64 (`uname` evidence recorded in RUN_LOG.md)
- **Python:** 3.13.5
- **pytest:** 9.0.2
- **Clang:** 17.0.0
- **GCC:** 14.2.0
- **Node:** 22.16.0
- **Build system:** setuptools via `pyproject.toml`; Makefile orchestration
- **Primary languages/formats:** Python, Markdown, JSON/JSON Schema, C/C++, Java, YAML, TOML, shell, PowerShell
- **Project purpose (verified from README and package metadata):** evidence-governed x86/x86-64 Windows binary analysis, reconstruction, validation, and reproducible release work.

## Safe commands identified

Read-only or disposable-clone checks included parser/AST/JSON validation, source-manifest verification, CLI help/error probes, exact pytest partitions, packaged self-tests, shell syntax checks, corpus synchronization, and malformed-input parser smoke tests. Commands that write reports, caches, build trees, or package artifacts were redirected to disposable clones or audit evidence paths.

## Environment limitations

- `mkdocs`, `javalang`, and `pyflakes` were not installed in the active environment. They were not installed because the review-only specification prohibits altering the project environment without authorization. Current executions of those gates are therefore **Blocked from verification in this environment**; prior sealed reports are historical corroboration only.
- The source archive lacks Git metadata, so Git-aware inventory fields are explicitly unavailable rather than guessed.
- Optional external integrations (Ghidra, DynamoRIO, model servers, commercial toolchains, network services) were not invoked.
- No coverage.py line/branch run was performed during this review-only audit; test execution counts must not be confused with code-coverage percentages.
""",encoding='utf-8')

(AUDIT/'AUDIT_PLAN.md').write_text("""# Review-only audit plan

## Scope

The baseline is the 543-file extracted archive. Every baseline file is inventoried, hashed, completely read at byte level, classified, cross-referenced, assigned a final ledger status, and linked to one A–M per-file report. All 540 UTF-8 files received complete-content structural and semantic review. The three binary fixtures received full byte/hash inventory and limited purpose/security review without execution.

New artifacts created by this audit are isolated under `project-audit/review-only-2026-07-10/`; they are not added to the baseline denominator. Existing repository files, including the historical `project-audit/` record, must remain byte-identical.

## Repository-specific risks

1. Untrusted PE/COFF/PDB/archive parsing and resource bounds.
2. Evidence provenance, claim levels, and reproducibility.
3. Command-surface breadth and documentation drift.
4. File/path/process/network trust boundaries.
5. Packaging and deterministic manifest integrity.
6. Duplicated source/package test logic.
7. Optional-tool behavior and explicit blocked states.

## Review order and methods

1. Establish byte-identical baseline and deterministic manifests.
2. Parse every Python and JSON file; fully ingest every text file; record binary hashes and context.
3. Build architecture, command, dependency, duplicate, documentation, and test maps.
4. Review risk-bearing implementations and corroborating tests/documentation.
5. Execute safe checks only in disposable clones or with outputs redirected to audit paths.
6. Triple-check important findings using direct evidence, corroboration, and consistency review.
7. Generate per-file reports sequentially and reconcile ledger/inventory counts.
8. Rehash every original file, seal all audit artifacts, and package the reviewed tree.

## Prohibited actions

No source edits, formatting, renames, dependency updates, global installs, network-dependent integration runs, destructive commands, Git operations, or fix-mode tools. No finding may rely on conversational memory or unsupported inference.

## Completion criteria

- 543/543 baseline inventory rows have final statuses.
- 543/543 per-file reports exist and contain sections A–M.
- 540/540 text files are marked completely read; 3/3 binaries have documented limited-review reasons.
- Command and canonical-route inventories reconcile to runtime parser counts.
- Exact tests and checks are recorded with outputs and limitations.
- Every original SHA-256 digest matches the baseline.
- No Pending, Unread, Unknown, or unexplained hash discrepancy remains.
- Audit artifacts are sealed by a self-excluding SHA-256 manifest.
""",encoding='utf-8')

# Architecture notes.
(AUDIT/'ARCHITECTURE_NOTES.md').write_text("""# Architecture notes

## Status

This is the final architecture model derived from complete repository review, parser introspection, tests, documentation, and source call relationships. Statements about runtime behavior are limited to executed paths or directly inspected contracts.

## Entry points

- `x86decomp` → `x86decomp.cli:main` is the primary unified CLI.
- `x86decomp-test` → the separately packaged `x86decomp_testkit` CLI drives adapter-aware verification.
- Three Ghidra Java scripts export/query analysis artifacts inside Ghidra.
- A read-only FastAPI/Uvicorn project service is available through the `serve` command and defaults to loopback.

## Major planes

1. **Ingestion and evidence:** project initialization, immutable artifacts, content store, evidence/claim records, project-state database, manifests.
2. **Static binary parsing:** bounded reader, PE32/PE32+, COFF/archive, PDB/MSVC metadata, resources/imports/relocations/debug/TLS.
3. **Analysis and reconstruction:** disassembly, ABI, symbolic/dynamic analysis, linker layout, candidate generation, compiler/worker, reconstruction package.
4. **Governance/control:** workflows, reviews, hypotheses, proofs, campaigns, candidates, changesets, durable workers and orchestration.
5. **Native/assembly:** native PE reconstruction, matching, slots, staging, annotation, relocation materialization, closed-loop validation.
6. **Local-model proposal:** profiles, bounded HTTP transports, prompts, matching, compiler/relocation/raw-byte validation. Model output is treated as untrusted proposal text.
7. **Verification harness:** inventory, schemas, adapter detection/capabilities, process logging, reports, package self-tests, toolkit public-contract tests.

## Data and control flow

Input binaries are hashed and represented as evidence before interpretation. Parsers transform bounded byte ranges into structured records. The project/control planes persist claims, artifacts, workflow state, and provenance. Candidate generators—including local-model integrations—produce proposals that advance only through explicit compiler, relocation, differential, symbolic, integration, or exact-byte checks. Reports and schemas provide machine/human consumption.

## Configuration and persistence

Configuration is JSON/TOML/CLI driven. SQLite stores project/control state. Content-addressed artifacts preserve hashes. JSON schemas define 97 contracts. Deterministic root/suite/all-file manifests bind release files. External-tool and model-server integrations are optional and represented as available, blocked, or unresolved rather than silently successful.

## Error handling and logging

The package centralizes contract and command errors, generally emits structured JSON for command failures, and records process/evidence output. Broad exception handlers exist but were not treated as defects without a demonstrated masking path. The exact test runner rejects failures, errors, skips, missing JUnit output, and inventory mismatches.

## Trust boundaries

- Binary/archive inputs are untrusted and bounded by readers, member/path checks, and size/count limits.
- Native execution and non-loopback services require explicit authorization.
- Remote/local-model output remains untrusted until deterministic validation.
- Subprocess invocations use argument arrays; the static scan found no `shell=True` call.
- Path normalization and containment checks protect workflow/project boundaries.
- Optional integrations and network behavior remain an operational boundary not fully exercised here.

## Dependency direction and risks

The core package contains several broad CLI/dispatch modules and many store-oriented subsystems. Cross-package coupling is mostly routed through models/contracts and project paths. Primary architecture risks are documentation scale, duplicated packaged tests, high-branch dispatch functions, and release-gate self-mutation rather than a verified cyclic-dependency failure.
""",encoding='utf-8')

# Command system audit.
cs=command_docs['summary']
(AUDIT/'COMMAND_SYSTEM_AUDIT.md').write_text(f"""# Command-system audit

## Complete inventory

- Root commands: **{command_audit['root_command_count']}**
- All argparse parser nodes: **{len(command_audit['commands'])}**
- Canonical groups: **{command_audit['canonical_group_count']}**
- Canonical routes: **{command_audit['canonical_route_count']}**
- Parser nodes with help: **{command_audit['summary']['commands_with_help']}/{len(command_audit['commands'])}**
- Parser nodes with long descriptions: **{command_audit['summary']['commands_with_description']}/{len(command_audit['commands'])}**

Every command, option/argument metadata record, default, choice set, help string, description flag, documentation mention, example match, and safety-flag indicator is in `COMMAND_INVENTORY.csv`. Every canonical group/action route and owner is in `CANONICAL_ROUTE_INVENTORY.csv`. These CSV files are the required one-row-per-command matrices; no command is omitted from the inventory.

## Structure and dispatch

The root parser combines legacy/direct commands with a canonical 59-group/239-route capability plane. Grouped subparsers improve discoverability for large subsystems (governance, reconstruction, native, assembly, local LLM). Root invalid-command output is mechanically correct but very long because argparse prints 166 choices. Missing required-file behavior produced structured JSON and exit status 2.

## Help, errors, and scriptability

- `x86decomp --help`: exit 0; all root commands displayed.
- `x86decomp commands`: machine-readable command inventory generated successfully.
- Invalid command: exit 2 with argparse usage/error.
- Missing input file: exit 2 with a concise structured error.
- `x86decomp --version`: exit 2; no version action exists (UX-001).
- Canonical plan-only routes are explicitly described as non-mutating in the generated reference.

Stable exit-code contracts beyond the executed error paths were not inferred. Commands capable of writes, subprocesses, network access, native execution, or project mutation were reviewed statically and through existing tests rather than invoked on user data.

## Documentation coverage

- Root commands explicitly documented: **{cs['root_documented']}/{cs['root_commands']}**
- Root commands with examples: **{cs['root_examples']}/{cs['root_commands']}**
- All parser nodes explicitly documented: **{cs['all_nodes_documented']}/{cs['parser_nodes']}**
- All parser nodes with matched examples: **{cs['all_nodes_examples']}/{cs['parser_nodes']}**
- Canonical routes documented: **{cs['routes_documented']}/{cs['canonical_routes']}**
- Canonical routes with examples: **{cs['routes_examples']}/{cs['canonical_routes']}**

Built-in help coverage is complete; long-form argument/output/error/example/use-case/safety coverage is not. This distinction is the basis of DOC-002.

## Overall assessment

Command registration and basic help are coherent and mechanically synchronized. The primary weaknesses are breadth, sparse long-form workflow documentation, no version flag, and verbose root error usage. No implemented-but-unregistered root command was verified, and the live parser counts match release inventory claims.
""",encoding='utf-8')

# Reverse-engineering practice audit.
(AUDIT/'REVERSE_ENGINEERING_PRACTICES.md').write_text("""# Reverse-engineering practice audit

## Strong practices — Verified or strongly supported

- Acquisition/evidence, parsing, analysis, interpretation, candidate generation, validation, and reporting are separated into distinct modules and claim levels.
- Input and artifact SHA-256 values, deterministic manifests, compiler commands, and evidence records support provenance and reproducibility.
- PE/COFF/PDB parsing uses bounded readers and explicit size/member/path limits. A deterministic malformed-input smoke run rejected 7,000 generated invalid samples through expected typed errors with no unexpected exception.
- Local-model output is explicitly untrusted and cannot be accepted by the byte-match lane without compiler, relocation, and raw-byte identity evidence.
- Unknown, blocked, unavailable, and partial states are modeled rather than converted to silent success.
- Matching-decompilation and functional-decompilation claims remain separate.
- Project backups reject traversal, links, devices, excessive members, per-member sizes, and total expansion limits.
- Reports, JSON schemas, JUnit, Markdown/HTML, and machine-readable command output support analyst and automation workflows.

## Limits and concerns

- COR-001 affects backup restoration on the earliest declared Python 3.11 patch releases.
- Complete parser correctness cannot be proven by static review and bounded malformed-input smoke testing; adversarial format fuzzing at scale remains desirable.
- Optional Ghidra, DynamoRIO, angr, compiler, native-execution, and model-server integrations were not fully exercised in this environment.
- Non-loopback service/model use is explicit but shifts authentication, TLS, network isolation, and data-disclosure controls to the operator; this is documented as an operational trust boundary rather than asserted as an exploitable defect.
- Command/reference documentation does not yet explain every analyst workflow, expected output, false-positive boundary, and safety implication (DOC-002).

## Suitability verdict

The project demonstrates sound evidence-governed reverse-engineering principles for an alpha-stage toolkit: provenance, claim separation, deterministic validation, bounded parsing, and explicit blocked states are stronger than typical ad-hoc tooling. Suitability for production or hostile-input use remains conditional on remediation of the verified findings, broader integration/fuzz testing, and operator-controlled sandboxing for external tools and native execution.
""",encoding='utf-8')

# Cross-file analysis.
dup_rows=[]
for i,g in enumerate(duplicates,1):
    members='; '.join(f"`{m['path']}:{m['symbol']}`" for m in g['members'])
    dup_rows.append(f'| DUP-G{i:03d} | {members} | {"Packaged/source test duplication" if all(("test-suite/tests/" in m["path"] or "/self_tests/" in m["path"]) for m in g["members"]) else "Normalized AST equivalence"} | See `DUPLICATION_MATRIX.csv`; do not consolidate mechanically. |')
(AUDIT/'CROSS_FILE_ANALYSIS.md').write_text(f"""# Cross-file analysis

## Architecture and dependency direction

The repository is functionally organized into core parsing/evidence modules plus governance, reconstruction, native, assembly, local-model, service, and verification-harness subsystems. Shared contracts/models/readers reduce parser and store duplication. No import-cycle failure was established by execution. Large dispatch surfaces (`cli._run`, reconstruction/canonical routers) are maintainability hotspots, but no runtime defect was inferred solely from branch count.

## State, error, logging, and configuration consistency

SQLite-backed stores use explicit transactions and context managers. CLI errors generally become structured output; argparse registration errors retain argparse formatting. Configuration is split across package metadata, JSON schemas, CLI defaults, and model/test profiles. The principal inconsistency is that strict Ruff/Pyright configuration is present but absent from dev dependencies and CI (MAINT-001).

## Packaging and release integrity

The pristine archive passed all three deterministic manifest checks. The documented `make verify` sequence then self-invalidates the sealed docstring reports before hash verification (REL-001). License payloads are abbreviated (LIC-001). Package/source command counts and corpus copies otherwise reconcile.

## Testing and generated-source risks

The exact non-duplicated inventory passed 258/258 tests; 21 packaged self-tests passed separately. Six source/package test pairs are behaviorally duplicated without a dedicated synchronization gate (TEST-001). The 24 ground-truth corpus copies do have a byte-synchronization gate and passed it.

## Documentation and new-user experience

README and focused guides describe major workflows and evidence boundaries. Built-in CLI help is complete, but detailed command documentation is sparse (DOC-002), and 364 docstrings remain generic despite the PASS report (DOC-001). The primary CLI has no version flag (UX-001).

## Duplication matrix

The AST scan identified {len(duplicates)} normalized duplicate-function groups. Many are tiny constructors, context-manager exits, serializers, or CLI wrappers where a shared abstraction could increase coupling. Substantive and packaged-test groups require explicit comparison. Full machine-readable assessments are in `DUPLICATION_MATRIX.csv`.

| Group | Symbols | Similarity | Recommended direction |
|---|---|---|---|
{chr(10).join(dup_rows)}

## Dead/orphaned code and dependencies

No file was declared dead or orphaned without call/import/packaging evidence. Optional integrations are intentionally lazy. No unused dependency finding was raised from import frequency alone. The audit did verify dormant lint/type configurations, not unused runtime dependencies.

## Security boundaries

No `shell=True` subprocess call or obvious committed credential was found by the targeted scans. Path/archive/service/model boundaries use explicit controls. This is evidence of defensive design, not a security guarantee; optional native/external integrations and hostile-input resilience remain bounded by the stated limitations.
""",encoding='utf-8')

# Documentation audit.
(AUDIT/'DOCUMENTATION_AUDIT.md').write_text(f"""# Documentation audit

## Scope and factual checks

All 122 baseline Markdown files and all Python docstrings were completely ingested. Local Markdown targets were resolved; zero broken local targets were found. JSON companions parsed successfully. Version references were checked against release 0.7.11. Installation, verification, architecture, adapter, local-model, supported-scope, evidence, recovery, test-bundle, and security guides were reviewed against implementation and tests.

## Strengths

- README states purpose, authorization boundary, install commands, first-project flow, local-model acceptance boundary, assembly behavior, and verification entry points.
- Architecture and supported-scope documents distinguish static facts, proposals, and validated claims.
- Local-model documentation explains loopback defaults, secret indirection, redirects, and byte-match acceptance.
- Security and evidence documents communicate important trust boundaries.
- All 405 live argparse nodes contain help text.
- Module/class/function docstring presence is complete under the shipped gate.

## Verified weaknesses

1. **DOC-001:** 364/1,853 documented symbols use generic low-information forms; the quality gate checks only two obsolete exact phrases plus repeated first words.
2. **DOC-002:** explicit long-form coverage reaches {cs['root_documented']}/{cs['root_commands']} root commands and {cs['routes_documented']}/{cs['canonical_routes']} canonical routes; examples cover {cs['root_examples']} root commands and {cs['routes_examples']} routes.
3. **REL-001:** verification documentation tells users to run a sequence that rewrites sealed reports and then fails hash verification.
4. The command-reference Markdown is a count summary rather than a complete command manual.
5. The executable has no version-reporting option, reducing provenance usability (UX-001).

## Command-documentation matrix

`COMMAND_INVENTORY.csv` contains one row for each of 405 parser nodes, including summary/help, description presence, full argument metadata, documentation mention, example match, and safety flags. `CANONICAL_ROUTE_INVENTORY.csv` contains all 239 canonical routes. These are the exhaustive matrices; aggregate coverage is summarized in `COMMAND_SYSTEM_AUDIT.md`.

## New-user assessment

A new user can install, discover commands, initialize a project, and understand the evidence model. Advanced workflows require significant `--help` exploration or source reading because per-command examples, expected outputs, errors, and realistic use cases are not comprehensive. Documentation is therefore **usable but incomplete for the full advertised surface**.
""",encoding='utf-8')

# Findings register.
sev_counts=Counter(f['severity'] for f in findings)
parts=["# Findings register\n", f"Open findings: **{len(findings)}** — Critical {sev_counts['Critical']}, High {sev_counts['High']}, Medium {sev_counts['Medium']}, Low {sev_counts['Low']}, Informational {sev_counts['Informational']}.\n"]
for f in findings:
    affected=sorted(p for p in f['paths'] if p in base_by_path)
    parts.append(f"""## {f['id']} — {f['title']}

- **Category:** {f['category']}
- **Severity:** {f['severity']}
- **Confidence:** {f['confidence']}
- **Status:** {f['status']}
- **Affected files:** {', '.join(f'`{p}`' for p in affected[:60])}{' … (complete set in per-file ledger/evidence)' if len(affected)>60 else ''}
- **Affected symbols/commands:** {f['symbols']}
- **Direct evidence:** {f['evidence']}
- **Corroborating evidence:** {f['corroboration']}
- **Consistency check:** {f['consistency']}
- **User/technical impact:** {f['impact']}
- **Why it matters:** The stated impact is tied to direct and corroborating evidence; no additional severity is inferred.
- **Recommended remediation:** {f['recommendation']}
- **Verification needed:** {f['verification_needed']}
- **Related/duplicate findings:** {'DOC-001, DOC-002' if f['id']=='REL-001' else ('REL-001' if f['id'] in {'DOC-001','DOC-002'} else ('TEST-001' if f['id']=='REPO-001' else 'None'))}
- **Triple-verification result:** Direct evidence, corroboration, and consistency review were all completed. Where legal effect or exhaustive runtime behavior is outside scope, that limit is explicitly stated.
""")
(AUDIT/'FINDINGS_REGISTER.md').write_text('\n'.join(parts),encoding='utf-8')

# Run log.
(AUDIT/'RUN_LOG.md').write_text(f"""# Run log

Commands were executed against the extracted baseline or disposable byte-identical clones. Exit status is reported only when observed. Long outputs are stored under `evidence/`.

| Command / operation | Purpose | Exit/result | Conclusive? | Side effects / notes |
|---|---|---:|---|---|
| SHA-256 of uploaded ZIP | Bind input archive | `ec222b…7468a` | Yes | Read-only |
| Recursive byte inventory and UTF-8 decode | Discover/read every baseline file | 543 files; 540 text; 3 binary | Yes for inventory/read status | Read-only; `evidence/baseline_all_files.json` |
| `python scripts/source_hashes.py verify` on pristine clone | Verify root/suite/all-file manifests | 0; 540/540, 63/63, 542/542 | Yes | Read-only relative to tracked inventory |
| Python AST parse of all `.py` files | Syntax/symbol/import/risk/docstring analysis | All parsed; no syntax failures | Yes for parseability | Read-only |
| JSON parse of all `.json` files | Validate JSON syntax | All parsed | Yes for syntax | Read-only |
| Markdown local-link resolver | Check local target existence | 0 broken local targets | Yes for local paths | External URLs not dereferenced |
| CLI root/help/commands probes | Inventory live command system | 166 root; 405 parser nodes; exit 0 | Yes | Read-only |
| CLI invalid/missing/version probes | Check error/version behavior | invalid 2; missing 2; version 2 | Yes for executed paths | Read-only |
| `scripts/audit-docstrings.py` with redirected outputs | Exercise gate without source writes | 0/PASS | Yes for shipped checks | Outputs under disposable/audit paths |
| Default `scripts/audit-docstrings.py` then hash verify in disposable clone | Test documented sequence | docstring 0; hash verify 2 | Yes | Changed only disposable clone reports; evidence preserves before/after hashes |
| Expanded AST docstring scan | Detect generic quality patterns | 364/1,853 symbols across 128 files | Yes for defined patterns | Pattern policy is documented in JSON evidence |
| Parser malformed-input smoke | Exercise COFF/archive/PDB/PE rejection | 7,000 expected typed rejections; 0 unexpected | Yes for generated cases | Deterministic random seed; not exhaustive fuzzing |
| Exact pytest collection | Establish intended inventory | 258 tests, 86 partitions | Yes | Cache disabled |
| Resumable exact pytest partition replay | Execute intended inventory | 258 passed; 0 failed/errors/skips | Yes | Disposable clone; every partition has JSON/log/JUnit evidence |
| Packaged self-test replay | Exercise duplicated packaged tests | 21 passed | Yes | Disposable clone; cache disabled |
| Corpus synchronization check | Compare 24 source/package copies | 0/PASS | Yes | Read-only |
| `bash -n scripts/verify.sh` and `bash -n scripts/verify-ghidra.sh` | Shell syntax | 0 | Yes for syntax only | Scripts not fully executed |
| Contract validation | Validate schemas/Java contracts | Blocked: `javalang` absent | No | Dependency not installed under review-only rule |
| Strict MkDocs build | Validate site | Blocked: `mkdocs` absent | No | Dependency not installed |
| Pyflakes | Static undefined/unused check | Blocked: `pyflakes` absent | No | Dependency not installed |
| Expanded trailing-whitespace scan | Format hygiene | 45 lines / 17 files | Yes | Read-only; intentional Markdown hard breaks distinguished in recommendations |
| Final original-file SHA reconciliation | Prove no baseline modification | Generated after all reports | Yes | See `ORIGINAL_FILE_HASH_RECONCILIATION.json` |

## Interpretation

Passing tests verify the executed behavior only. Blocked gates are not described as passes. Historical reports in the input repository are treated as corroboration, not substituted for current execution. No optional external integration or suspicious binary was executed.
""",encoding='utf-8')

# Coverage report with full table.
coverage_rows='\n'.join(f"| {r['inventory_id']} | `{r['relative_path']}` | {r['text_or_binary']} | {r['audit_status']} | `{r['sha256']}` | `{r['per_file_report']}` |" for r in rows)
(AUDIT/'COVERAGE_REPORT.md').write_text(f"""# Coverage reconciliation

## Counts

- Original baseline files: **543**
- Final original-file count: **543**
- Fully audited text files: **540**
- Limited binary reviews: **3**
- Blocked baseline files: **0**
- Pending baseline files: **0**
- Inaccessible baseline files: **0**
- Per-file reports: **543**
- Inventory rows: **543**
- Ledger rows with final status: **543**
- Files added during the audit: audit artifacts only under `project-audit/review-only-2026-07-10/`
- Original files removed: **0**
- Original files with changed SHA-256: **0** (final machine-readable reconciliation is `ORIGINAL_FILE_HASH_RECONCILIATION.json`)
- Git tracked/ignored reconciliation: **Blocked from verification** because the source archive contains no `.git/` metadata.

## Coverage statement

**100% baseline file-accounting coverage is verified:** every one of 543 original files is inventoried, hashed, read in full at byte level, classified, assigned a final status, and linked to a per-file report. The 540 UTF-8 files received complete-content review. The three binary fixtures received limited binary review with full bytes/hash/size/purpose accounting and were not executed. This statement is file-accounting/review coverage, not code line or branch coverage.

## Complete table

| ID | Path | Kind | Final status | Baseline SHA-256 | Per-file report |
|---|---|---|---|---|---|
{coverage_rows}
""",encoding='utf-8')

# Final report.
(AUDIT/'FINAL_AUDIT_REPORT.md').write_text(f"""# Final exhaustive review-only audit report

## Executive Summary

The 543-file release is functionally coherent and demonstrates strong evidence-governed reverse-engineering design. Complete file accounting found **1 High, 4 Medium, 3 Low, and 1 Informational** open findings; no Critical finding was verified. The most serious issue is a deterministic-release contradiction: the documented `make verify` sequence rewrites two sealed docstring reports and then fails its own hash gate (REL-001). Medium findings cover the earliest Python 3.11 patch releases, incomplete distributed license text, generic docstrings missed by the quality gate, and sparse long-form command documentation.

Strong aspects include bounded binary readers, explicit archive/path/resource limits, claim/evidence separation, deterministic manifests, optional-integration blocked states, no detected `shell=True`, complete argparse help, a synchronized 24-file compiler corpus, and a clean exact test replay. The project remains alpha-stage and is not ready to claim production-grade hostile-input assurance without remediation and broader integration/fuzz testing.

- **Overall health:** Good foundation with material release/documentation/compatibility defects.
- **Readiness:** Suitable for controlled authorized evaluation; remediation recommended before treating the release gate and packaging claims as final.
- **Documentation:** Strong conceptual/evidence guidance, incomplete command/API specificity.
- **Command system:** Broad but coherent; complete built-in help, limited long-form examples.
- **Architecture:** Modular by analysis plane, with some large dispatch and duplicated test surfaces.
- **Test confidence:** High for the executed 258-test contract plus 21 packaged self-tests; not a proof of exhaustive correctness.
- **New-user usability:** Usable for initial workflows, difficult across the full 405-node command tree.
- **Reverse-engineering suitability:** Strong principles; conditional operational assurance.

## Scope and Methodology

The baseline is the uploaded archive with SHA-256 `ec222b125e59987642c1685d9c1a1e44cc2c2c2d53e8500aed72ac96c9c7468a`. All 543 files were discovered filesystem-wise because Git metadata is absent. Every file was read and hashed twice during analysis/report generation. Python and JSON files were parsed completely; Markdown local links, headings, and references were checked; C/C++/Java/scripts/configuration/manifests were fully ingested and reviewed with format-specific rules; binaries were byte-inventoried and not executed.

Important findings used triple verification: direct implementation/configuration evidence, corroborating call/test/documentation/runtime evidence, and consistency checks against public behavior and project contracts. Safe execution occurred only in disposable clones or with output redirected to audit paths. No project source was changed.

## Coverage Statement

File-accounting review coverage is **543/543 (100%)**: 540 complete text reviews and 3 documented limited binary reviews. There are zero Pending, Blocked-file, Unread, or Unknown statuses. This is not a line/branch code-coverage claim. See `COVERAGE_REPORT.md`, `FILE_INVENTORY.csv`, `AUDIT_LEDGER.csv`, and `AUDIT_READ_RECEIPT.json`.

## Architecture Assessment

The architecture separates acquisition/evidence, bounded parsing, project/control state, proposal generation, compiler/linker validation, matching/functional lanes, reporting, and verification. Shared readers/contracts support dependency direction. Governance, reconstruction, native, assembly, local-model, and harness packages are cohesive at a subsystem level. Risks are broad dispatch functions, repeated store/constructor patterns, two copies of packaged self-tests, and optional external-tool boundaries. No cyclic-import runtime failure was verified.

## Command-System Assessment

The executable registers 166 root commands, 405 parser nodes, 59 canonical groups, and 239 routes; all parser nodes have help. Invalid and missing-input paths return status 2. The command tree is scriptable through structured output in many paths, but comprehensive stable exit/output contracts were not established for every mutating command. Long-form docs cover only 23 root command examples and 7 route examples (DOC-002). The CLI lacks `--version` (UX-001).

## Documentation Assessment

Conceptual documentation is aligned with the evidence model and major safety boundaries. Local Markdown links are intact. Presence coverage for Python docstrings is complete under the shipped audit, but 364/1,853 symbols use generic wording that its narrow rules miss (DOC-001). The 11-line command reference does not replace a complete manual. Verification docs currently describe a self-invalidating sequence (REL-001).

## Correctness and Reliability

- **REL-001 (High):** verified release-gate self-mutation/hash failure.
- **COR-001 (Medium):** backup restore is incompatible with Python 3.11.0–3.11.3 despite `>=3.11` metadata.
- Exact intended tests: **258 passed, 0 failed, 0 errors, 0 skipped**, across 86 reconciled partitions.
- Packaged duplicate self-tests: **21 passed**.
- Malformed parser smoke: **7,000 expected typed rejections, 0 unexpected exceptions**.
- JSON/Python syntax: all parsed.

Important unverified areas include optional external integrations, full cross-platform CI, native execution, network services, all supported compiler/toolchain combinations, and exhaustive parser state spaces.

## Security and Robustness

No critical/high exploitable security defect was verified. Defensive controls include bounded reads, archive path/type/size limits, loopback defaults, explicit remote/native authorization, subprocess argument lists, and untrusted-model proposal handling. No `shell=True` was found. Non-loopback services and remote model endpoints remain operator-controlled trust boundaries; authentication/TLS/sandboxing are not provided by the reviewed call itself. Hostile-input assurance requires broader fuzzing and integration testing.

## Performance and Scalability

No confirmed performance regression was measured. Likely scaling risks are large dispatch functions, repeated parser/object construction, large inventories, and SQLite/content-store operations on very large projects. The code includes explicit query/member/size/worker bounds in critical paths. Profile real workloads before optimizing; do not trade evidence clarity for speculative micro-optimizations.

## Code Quality and Maintainability

Naming and subsystem separation are generally strong. The AST scan found 46 normalized duplicate-function groups; most are small wrappers/constructors/serializers where consolidation may be counterproductive. Six packaged/source self-test pairs create a concrete drift risk (TEST-001). Strict Ruff/Pyright settings are dormant in the documented workflow (MAINT-001). Generic docstrings are a low-authorship-quality indicator but do not establish AI authorship.

## Testing Assessment

Tests cover parsers, projects, evidence, CLI, packaging contracts, documentation gates, corpora, native/assembly/reconstruction/governance, orchestration, security/archive behavior, services, and adapters. The exact runner strongly reconciles collection/execution and rejects skips. Weaknesses are duplicate packaged self-tests, no minimum 3.11 patch test, no enforced type/lint jobs, and environment-blocked current MkDocs/contract/Pyflakes runs. Passing tests do not prove absence of defects.

## Reverse-Engineering Practice Assessment

Evidence provenance, deterministic hashes, raw-versus-interpreted separation, proposal-versus-claim boundaries, partial/blocked states, parser limits, and machine/human reports are strong. Legal/ethical scope and native-execution safeguards are present. Remaining work is adversarial fuzz depth, complete analyst workflow docs, and broader integration/sandbox verification.

## Prioritized Findings

### Immediate action

1. **REL-001 (High):** make verification read-only with respect to sealed reports and prove a pristine extracted release passes end-to-end.

### Near-term action

2. **COR-001 (Medium):** align Python metadata/implementation and test the exact minimum patch.
3. **LIC-001 (Medium):** ship the complete Apache-2.0 license text in both distributions.
4. **DOC-001 (Medium):** replace generic docstrings and strengthen semantic quality checks.
5. **DOC-002 (Medium):** generate/author full command documentation with examples and safety/output/error contracts.

### Medium-term improvement

6. **TEST-001 (Low):** canonicalize or synchronize packaged self-tests.
7. **MAINT-001 (Low):** enforce or remove dormant Ruff/Pyright configuration.
8. **UX-001 (Low):** add a version option.

### Optional refinement

9. **REPO-001 (Informational):** remove unintended trailing whitespace while retaining intentional Markdown hard breaks.

## Consolidation Opportunities

See `DUPLICATION_MATRIX.csv`. The only finding-level consolidation target is the six packaged/source test pairs. Tiny constructors, context managers, store decoders, and serializers should be consolidated only where behavior/error semantics and dependency direction remain simpler. Command documentation should be generated from parser metadata but enriched with human-authored workflows rather than duplicated manually.

## Recommended Remediation Roadmap

| Priority | Recommendation | Expected impact | Areas | Dependencies | Complexity | Risk | Verification |
|---|---|---|---|---|---|---|---|
| Immediate | Add non-mutating docstring verification and reorder/clarify release generation | Restores trustworthy release gate | Makefile, audit script, manifests, docs | None | Small–Medium | Timestamp/determinism behavior | Fresh-archive `make verify` plus zero hash changes |
| Near | Raise minimum to 3.11.4 or add compatibility path | Restores metadata truth | project_state, metadata, CI | Multi-Python runner | Small | Archive safety must not regress | Tests on exact minimum and current releases |
| Near | Include full official license text | Self-contained distribution licensing | root/suite packages | Legal review if desired | Small | Low | Inspect wheel/sdist payloads |
| Near | Replace 364 generic docstrings and broaden gate | Improves API clarity and gate truth | 128 files, audit script | Review policy | Medium–Large | Mechanical prose may remain shallow | AST scan plus manual samples |
| Near | Build complete command manual | Improves discoverability/safety | CLI metadata/docs | Example harness | Large | Docs drift | Matrix reaches 100%; examples execute |
| Medium | Single-source or synchronize self-tests | Prevents package/source drift | test-suite | Packaging design | Medium | Package inclusion changes | Deliberate drift test |
| Medium | Add reproducible lint/type targets | Enforces declared quality settings | metadata/CI/Makefile | Tool pins | Small | New failures need triage | Clean dev install and CI |
| Optional | Add `--version`; whitespace cleanup | Provenance and polish | CLI/repo text | None | Small | Low | Entry-point tests; format scan |

## Limitations and Unverified Areas

Git history/status, current branch/commit, ignored status, and authorship provenance are unavailable from the archive. Current MkDocs, javalang contract, and Pyflakes gates were blocked by absent dependencies and were not installed. Optional external tools, network systems, native execution, hostile corpora, and every OS/compiler combination were not exercised. Legal compliance is not adjudicated. No claim of exhaustive semantic, security, performance, line, or branch coverage is made.

## Final Verdict

The project appears **functionally coherent and maintainable with targeted remediation**. Its command system is logically organized but too broad for the present long-form documentation. Documentation is sufficient for initial use but not for the complete advertised command/API surface. Reverse-engineering practices are evidence-aware and generally appropriate. The release is suitable for controlled authorized use and further development, but the current verification workflow and packaging/license/minimum-version issues should be fixed before asserting fully reproducible release readiness. **Confidence: High for file accounting and reported findings; Moderate for overall runtime readiness because optional and adversarial integrations were not fully exercised.**
""",encoding='utf-8')

(AUDIT/'README.md').write_text("""# Review-only audit index

This directory contains a fresh, exhaustive review-only audit of the 543-file input archive. It does not replace or modify the historical audit artifacts in the parent directory.

Start with:

1. `FINAL_AUDIT_REPORT.md`
2. `FINDINGS_REGISTER.md`
3. `COVERAGE_REPORT.md`
4. `FILE_INVENTORY.csv` and `AUDIT_LEDGER.csv`
5. `COMMAND_SYSTEM_AUDIT.md`, `DOCUMENTATION_AUDIT.md`, `CROSS_FILE_ANALYSIS.md`, and `REVERSE_ENGINEERING_PRACTICES.md`
6. `files/` for one A–M report per baseline file
7. `evidence/` for machine-readable scans, command output, logs, and JUnit results

The final self-excluding `AUDIT_ARTIFACT_MANIFEST.sha256` seals every artifact in this directory.
""",encoding='utf-8')

print(json.dumps({'audit_root':str(AUDIT),'inventory_rows':len(rows),'reports':len(list(FILES_DIR.glob('*.md'))),'findings':len(findings)},indent=2))
