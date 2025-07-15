#!/usr/bin/env python3
from pathlib import Path
import frontmatter

CONTENT_ROOT = Path('.')
OUTPUT_DIR   = Path('docs')
INDEX_FILE   = OUTPUT_DIR / 'index.md'

md_files = sorted(
    p for p in CONTENT_ROOT.rglob('*.md')
    if p != INDEX_FILE
)

lines = ['# Process Directory', '']
for md in md_files:
    rel = md.as_posix()
    try:
        post = frontmatter.load(md)
        title = post.get('title', md.stem.replace('_', ' '))
    except:
        title = md.stem.replace('_', ' ')
    lines.append(f'- [{title}]({rel})')

OUTPUT_DIR.mkdir(exist_ok=True)
INDEX_FILE.write_text('\n'.join(lines) + '\n', encoding='utf-8')
print(f'✅ Wrote directory to {INDEX_FILE}')
