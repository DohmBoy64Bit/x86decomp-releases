#!/usr/bin/env python3
"""Parse every documented x86decomp command against an extracted v0.7.4 CLI parser."""
from __future__ import annotations
import argparse, contextlib, html.parser, io, json, shlex, sys
from pathlib import Path

class CodeParser(html.parser.HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.depth=0; self.parts=[]; self.blocks=[]
    def handle_starttag(self,tag,attrs):
        if tag=='code':
            if self.depth==0:self.parts=[]
            self.depth+=1
    def handle_endtag(self,tag):
        if tag=='code' and self.depth:
            self.depth-=1
            if self.depth==0:self.blocks.append(''.join(self.parts))
    def handle_data(self,data):
        if self.depth:self.parts.append(data)

def main() -> int:
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('source_root',type=Path)
    ap.add_argument('--pages-root',type=Path)
    args=ap.parse_args()
    source=args.source_root.resolve()
    pages=(args.pages_root or (Path(__file__).resolve().parent/'payload')).resolve()
    sys.path.insert(0,str(source/'src'))
    from x86decomp.cli import _build_parser
    parser=_build_parser(); commands=[]; failures=[]
    for page in sorted(pages.rglob('*.html')):
        hp=CodeParser();hp.feed(page.read_text(encoding='utf-8'))
        for block in hp.blocks:
            for lineno,line in enumerate(block.splitlines(),1):
                text=line.strip()
                if not text.startswith('x86decomp '):continue
                commands.append({'page':str(page.relative_to(pages)),'line':lineno,'command':text})
                try:
                    tokens=shlex.split(text,posix=True)
                    tokens=['0x401230' if t=='$targetBase' else t for t in tokens]
                    with contextlib.redirect_stderr(io.StringIO()),contextlib.redirect_stdout(io.StringIO()):
                        parser.parse_args(tokens[1:])
                except (ValueError,SystemExit) as exc:
                    failures.append({'page':str(page.relative_to(pages)),'line':lineno,'command':text,'error':str(exc)})
    result={'format':'x86decomp-project-examples-command-surface-verification-v1','target_release':'0.7.4','source_root':str(source),'pages_root':str(pages),'command_lines_checked':len(commands),'unique_commands':len({c['command'].split()[1] for c in commands}),'status':'pass' if not failures else 'fail','failures':failures}
    print(json.dumps(result,indent=2));return 0 if not failures else 2
if __name__=='__main__':raise SystemExit(main())
