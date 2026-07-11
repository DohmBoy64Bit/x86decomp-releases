from pathlib import Path
import os,random,tempfile,json,sys
ROOT=Path('/mnt/data/x86decomp-audit-work/x86decomp-toolkit-0.7.11');sys.path.insert(0,str(ROOT/'src'))
from x86decomp.coff import parse_coff_bytes
from x86decomp.coff_archive import parse_coff_archive_bytes
from x86decomp.pdb import parse_pdb_bytes
from x86decomp.pe import parse_pe
from x86decomp.errors import X86DecompError
rng=random.Random(0x86DEC0DE)
parsers={'coff':parse_coff_bytes,'archive':parse_coff_archive_bytes,'pdb':parse_pdb_bytes}
res={}
for name,fn in parsers.items():
 unexpected=[]; accepted=0; expected=0
 for i in range(2000):
  n=rng.randrange(0,4097); b=rng.randbytes(n)
  try: fn(b); accepted+=1
  except (X86DecompError,OSError,ValueError): expected+=1
  except Exception as e: unexpected.append({'i':i,'size':n,'type':type(e).__name__,'message':str(e)})
 res[name]={'accepted':accepted,'expected_rejections':expected,'unexpected':unexpected}
# PE paths: random plus structured MZ prefixes
unexpected=[];accepted=0;expected=0
with tempfile.TemporaryDirectory() as td:
 for i in range(1000):
  n=rng.randrange(0,4097); b=bytearray(rng.randbytes(n))
  if n>=2 and i%2==0:b[:2]=b'MZ'
  p=Path(td)/f'{i}.bin';p.write_bytes(b)
  try:parse_pe(p);accepted+=1
  except (X86DecompError,OSError,ValueError):expected+=1
  except Exception as e:unexpected.append({'i':i,'size':n,'type':type(e).__name__,'message':str(e)})
res['pe']={'accepted':accepted,'expected_rejections':expected,'unexpected':unexpected}
Path('/mnt/data/x86decomp-audit-external/parser-fuzz-smoke.json').write_text(json.dumps(res,indent=2)+'\n')
print(json.dumps(res,indent=2)[:8000])
raise SystemExit(1 if any(v['unexpected'] for v in res.values()) else 0)
