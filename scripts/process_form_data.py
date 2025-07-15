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
    """Determine subfolder name based on known Section/Category QIDs for each repo branch."""
    keys = [
        # 1. Handbook branch
        "r193faaedd19c49669e0600e0d11edfca",  # 120_LinuxDaemons
        # 2. Handbook Companion branch
        "rde080b09b05a47deb4c1111ff7ffc068",  # 130_GeospatialTechniques
        # 3. Project Specific Processes branch
        "r3a4399885e004123ad9c270fa3509b3a",  # 110_RAMS
        # 4. Data Repository branch
        "r1198559f25ba43629596c31ea3496e27",  # 600_Tabular_Data
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
# Dynamically detect all step QIDs (major/detail) beyond core metadata
import re
core_qids = {
    # Metadata and section keys
    "r4a93806b735947948cb4f64ac6b88d1d",
    "r193faaedd19c49669e0600e0d11edfca",
    "r1198559f25ba43629596c31ea3496e27",
    "r37c0831ebc6748c688ffad033a5b12d8",
    "r3a4399885e004123ad9c270fa3509b3a",
    # Frontmatter keys
    "r090df130b6a14e4da6842248a6fd9292",
    "rb161d63d7baa4ffb9f61ac63846ca8c8",
    "r5bc371d4242c4f09b7b7980d18211809",
    "r66c909f82883482fa07d3462e89e01e1",
    "rb84d93fdf65d4fa89c1dc0796adc1607",
    "rba00b055bbf9454f83bec1ec4f37c0c8",
    "rc94139595a2c485c9a5cde963d202637",
    # System keys
    "submitDate",
    "responder"
}
# Collect all potential step QIDs preserving original form order
all_step_qids = [
    q for q in row.keys()
    if re.fullmatch(r"r[0-9a-f]{32}", q)
    and q not in core_qids
]
# Filter only those with non-empty answers, so we ignore unanswered steps
step_qids = [q for q in all_step_qids if get_value(q)]

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
# Populate steps table from dynamic step_qids
for i in range(0, len(step_qids), 2):
    step_num = i // 2 + 1
    maj_q = step_qids[i]
    det_q = step_qids[i+1] if i+1 < len(step_qids) else None
    maj = get_value(maj_q)
    det = get_value(det_q) if det_q else ''
    if maj:
        lines.append(f"| {step_num} | {maj} | {det or 'N/A'} |")

# === WRITE FILE ===
out_file.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"✅ Created: {out_file}")
