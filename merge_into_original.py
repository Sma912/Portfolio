#!/usr/bin/env python3
"""Non-destructive portfolio merge utility. Requires Python 3.8+; no dependencies."""
from pathlib import Path
import argparse, shutil, zipfile, tempfile, re, sys
SRC=Path(__file__).resolve().parent
files=['assets/portfolio-writing.css','assets/portfolio-writing-addon.js','writing/index.html','writing/backlinks-vs-referring-domains/index.html','writing/revivio-marketing-copy/index.html','downloads/SEO_Backlinks_Referring_Domains_Morteza_Ahmadi.pdf','downloads/Revivio_Marketing_Copy_Morteza_Ahmadi.pdf']
p=argparse.ArgumentParser(description='Merge writing portfolio content into existing static website')
p.add_argument('original', help='Original static website directory or ZIP including index.html')
p.add_argument('--output', required=True,help='Output complete ZIP file, does not overwrite original')
a=p.parse_args()
out=Path(a.output).resolve();origin=Path(a.original).resolve()
if not origin.exists():sys.exit('Original website not found: '+str(origin))
with tempfile.TemporaryDirectory(prefix='portfolio_merge_') as tmp:
    root=Path(tmp)/'site';root.mkdir()
    if origin.is_dir():shutil.copytree(origin,root,dirs_exist_ok=True)
    else:
        with zipfile.ZipFile(origin) as z:
            for item in z.infolist():
                target=(root/item.filename).resolve()
                if not target.is_relative_to(root.resolve()):sys.exit('Unsafe path in ZIP; merge aborted')
                z.extract(item,root)
    ix=list(root.rglob('index.html'))
    if (root/'index.html').exists():site=root
    elif len(ix)==1:site=ix[0].parent
    else:sys.exit('Cannot safely identify site root; expected one index.html')
    html_file=site/'index.html';html=html_file.read_text(encoding='utf-8-sig')
    if '</head>' not in html.lower() or '</body>' not in html.lower():sys.exit('Invalid existing index.html structure; no changes made')
    for rel in files:
        dest=site/rel;dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(SRC/rel,dest)
    if '/assets/portfolio-writing.css' not in html:
        html=re.sub(r'</head>',r'  <link rel="stylesheet" href="/assets/portfolio-writing.css">\n</head>',html,count=1,flags=re.I)
    if '/assets/portfolio-writing-addon.js' not in html:
        html=re.sub(r'</body>',r'  <script defer src="/assets/portfolio-writing-addon.js"></script>\n</body>',html,count=1,flags=re.I)
    html_file.write_text(html,encoding='utf-8')
    out.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(out,'w',compression=zipfile.ZIP_DEFLATED) as z:
        for f in site.rglob('*'):
            if f.is_file():z.write(f,f.relative_to(site))
    print(f'Created: {out} ({out.stat().st_size:,} bytes)')
    print('Original site contents preserved; new writing content added.')
