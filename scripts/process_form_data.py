#!/usr/bin/env python3
import json
from pathlib import Path
from datetime import datetime

# === CONFIGURATION ===
JSON_PATH = Path("data/Template for Processes.json")  # raw JSON filepath

# === LOAD JSON ===
if not JSON_PATH.exists():
    raise FileNotFoundError(f"JSON not found: {JSON_PATH}")
with JSON_PATH.open("r", encoding="utf-8") as f:
    row = json.load(f)

# === HELPER ===
def get_value(key: str) -> str:
    """Retrieve and clean a value or join lists into comma-separated strings."""
    val = row.get(key, "")
    if isinstance(val, list):
        return ", ".join(map(str, val)).strip()
    return str(val or "").strip()

# === SECTION FOLDER ===
# Determine subfolder from the Section/Category1 field
def determine_section() -> str:
    keys = [
        "r193faaedd19c49669e0600e0d11edfca",
        "r1198559f25ba43629596c31ea3496e27",
        "r37c0831ebc6748c688ffad033a5b12d8",
        "r3a4399885e004123ad9c270fa3509b3a",
    ]
    for qid in keys:
        sec = get_value(qid)
        if sec:
            return sec
    return "Uncategorized"

section = determine_section()

# === METADATA KEYS ===
meta = {
    'title':   get_value("r090df130b6a14e4da6842248a6fd9292"),  # Process Title
    'number':  get_value("rb161d63d7baa4ffb9f61ac63846ca8c8"),  # Process Number
    'author':  get_value("r5bc371d4242c4f09b7b7980d18211809"),  # Created by
    'period':  get_value("r66c909f82883482fa07d3462e89e01e1") or "3 years",  # Review Period
    # Purpose may be under one of two QIDs depending on form branch
    'purpose': get_value("rb84d93fdf65d4fa89c1dc0796adc1607") or get_value("rba00b055bbf9454f83bec1ec4f37c0c8") or get_value("rc94139595a2c485c9a5cde963d202637"),
    'date':    get_value("submitDate"),                            # submission timestamp
}

# === STEP QID PAIRS ===
STEP_QIDS = [
    ("r97dc9b3936644c09a527fade2a8c2ced", "red79e9ae2dd9425094c408007e8b418f"),
    ("r7550fae0cae6497b9f5dd065a99619f1", "r2429caa9d171400e9402ac4a1f3711b8"),
    ("r5d174ef37c3748f2bb6bdc7b7e516320", "r46109de2e30f43bd9de65e780a6a1fb0"),
    ("r4d3e2edb08e641989b75f707b2fe6309", "r717d8c1016494e5f8c2ab2f928a241f1"),
    ("re8ef70bea24d437c8efb8585bff53103", "rb72f6c9b3e4341fdab95ce6b2e13a0a3"),
    ("r64df0d8c46eb4827b9a3e51185ba617f", "ra5fdba2bb0124de5bb507e2edd242c94"),
    ("rb8d21bdbc1d34bac9e332dcd60dc496d", "rea07d74a41e24afe8c01a29aeeae09c7"),
    ("rb97c2fe3e3b94c6fad7c7c4269aeadb9", "r4c3eb873609241f48c17ee59e463a66e"),
    ("r324e05d543d6479090b5674b19d1ccff", "r2946ad67113f46e581c4943371f83e52"),
    ("r149b262948be4658ae6851737328b25e", "rfa6ab87b34d9411eb257779d011f3e27"),
]

# === OUTPUT PATH ===
# Create section folder (if missing) under repo root
out_dir = Path(section)
out_dir.mkdir(parents=True, exist_ok=True)
filename = f"{meta['number'].replace(' ','_')}_{meta['title'].replace(' ','_')}.md"
out_file = out_dir / filename

# === BUILD MARKDOWN CONTENT ===
lines = [
    '---',
    f"title: {meta['title']}",
    f"author: {meta['author']}",
]
# Normalize date to ISO format if possible
try:
    dt = datetime.fromisoformat(meta['date'])
    lines.append(f"date: {dt.isoformat()}")
except ValueError:
    lines.append(f"date: {meta['date']}")
lines += [
    f"review_period: {meta['period']}",
    '---',
    '',
    '## Purpose',
    meta['purpose'] or 'N/A',
    '',
    '## Steps',
    '',
    '| Step | Major Activity | References, Forms and Details |',
    '|------|----------------|-------------------------------|',
]
# Populate steps table
for idx, (maj_q, det_q) in enumerate(STEP_QIDS, start=1):
    maj = get_value(maj_q)
    if not maj:
        continue
    det = get_value(det_q) or 'N/A'
    lines.append(f"| {idx} | {maj} | {det} |")

# === WRITE FILE ===
out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅ Created: {out_file}")
