import pandas as pd
from pathlib import Path

# === CONFIG ===
EXCEL_PATH = Path("data/Template for Processes.xlsx")
OUTPUT_DIR = Path("handbook.md")

# === LOAD DATA ===
df = pd.read_excel(EXCEL_PATH)
df.columns = [col.replace("\xa0", " ").strip() for col in df.columns]  # Normalize headers

for index, row in df.iterrows():
    folder_type = str(row.get("Pick a Folder", "")).strip()

    # Determine subfolder based on folder type
    if folder_type == "1. Handbook":
        subfolder = str(row.get("Section/Category", "")).strip()
    elif folder_type == "2. Handbook Companion":
        subfolder = str(row.get("Section/Category1", "")).strip()
    elif folder_type == "3. Project Specific Processes":
        subfolder = str(row.get("Section/Category2", "")).strip()
    elif folder_type == "4. Data Repository":
        subfolder = str(row.get("Section/Category3", "")).strip()
    else:
        subfolder = "Uncategorized"

    # Clean folder names
    folder_path = OUTPUT_DIR / folder_type.replace("/", "-").strip() / subfolder.replace("/", "-").strip()

    # Build file name: processNumber_processTitle.md
    process_number = str(row.get("Process Number", "")).strip()
    process_title = str(row.get("Process Title", "")).strip()
    safe_title = process_title.replace(" ", "_").replace("/", "-")
    filename = f"{process_number}_{safe_title}.md"
    file_path = folder_path / filename

    # Skip existing
    if file_path.exists():
        continue

    # Gather other fields
    created_by = str(row.get("Created by", "")).strip()
    review_period = str(row.get("Review Period", "")).strip()
    purpose = str(row.get("Purpose", "")).strip()

    # === Build Markdown ===
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
        major = str(row.get(f"Step {i}: Major Activity", "")).strip()
        detail = str(row.get(f"Step {i}: References, Forms and Details", "")).strip()

        if major and major.lower() != "nan":
            clean_major = major.replace("|", "\\|")
            clean_detail = (detail or "N/A").replace("|", "\\|")
            md += f"| {i} | {clean_major} | {clean_detail} |\n"

    # Save
    folder_path.mkdir(parents=True, exist_ok=True)
    file_path.write_text(md.strip() + "\n", encoding="utf-8")
