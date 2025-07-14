import pandas as pd
from pathlib import Path

# === CONFIG ===
EXCEL_PATH = Path("data/Template for Processes.xlsx")
OUTPUT_DIR = Path(".")

# === LOAD & NORMALIZE ===
df = pd.read_excel(EXCEL_PATH)
df.columns = [c.replace("\xa0", " ").strip() for c in df.columns]

# Sort by most recent completion time and take the newest entry
df = df.sort_values("Completion time", ascending=False)
latest_row = df.iloc[0:1]

for idx, row in latest_row.iterrows():
    # Validate and clean folder type
    folder_type = str(row.get("Pick a Folder", "")).strip()
    if not folder_type or folder_type.lower() == "nan":
        print("⚠️ Skipped row due to missing 'Pick a Folder'")
        continue

    # Extract metadata
    section1        = str(row.get("Section/Category1", "")).strip()
    process_title   = str(row.get("Process Title", "")).strip()
    process_number  = str(row.get("Process Number", "")).strip()
    created_by      = str(row.get("Created by", "")).strip()
    review_period   = str(row.get("Review Period", "")).strip()
    purpose         = str(row.get("Purpose", "")).strip()

    section_folder = section1 or "Uncategorized"

    # Safe filename
    safe_number = process_number.replace(" ", "_").replace("/", "-")
    safe_title  = process_title.replace(" ", "_").replace("/", "-")
    filename    = f"{safe_number}_{safe_title}.md"

    # Target path
    folder_path = Path(section_folder)
    file_path   = folder_path / filename

    print(f"→ Writing to: {file_path}")

    # Log even if it's overwriting
    if file_path.exists():
        print(f"  • Overwriting existing file")


    folder_path.mkdir(parents=True, exist_ok=True)

    # Markdown generation
    md = f"""---
title: {process_title}
author: {created_by}
date: {row.get('Start time', '')}
review_period: {review_period or '3 years'}
---

## Purpose
{purpose}

## Steps

| Step | Major Activity | References, Forms and Details |
|------|----------------|-------------------------------|
"""

    for i in range(1, 21):
        major = row.get(f"Step {i}: Major Activity", "")
        detail = row.get(f"Step {i}: References, Forms and Details", "")
        if isinstance(major, str) and major.strip():
            md += f"| {i} | {major.strip()} | {str(detail).strip() or 'N/A'} |\n"

    file_path.write_text(md, encoding="utf-8")
    print(f"✅ Created: {file_path}")
