import os
import pandas as pd
from pathlib import Path

# === CONFIG ===
EXCEL_PATH = "data/Template for Processes.xlsx"
OUTPUT_DIR = Path("handbook.md")

# === LOAD DATA ===
df = pd.read_excel(EXCEL_PATH)

# Normalize column headers
df.columns = [col.replace("\xa0", " ").strip() for col in df.columns]

for index, row in df.iterrows():
    folder_type = str(row.get("Pick a Folder", "")).strip()
    section1 = str(row.get("Section/Category", "")).strip()
    section2 = str(row.get("Section/Category1", "")).strip()
    section3 = str(row.get("Section/Category2", "")).strip()
    section4 = str(row.get("Section/Category3", "")).strip()
    process_title = str(row.get("Process Title", "")).strip()
    process_number = str(row.get("Process Number", "")).strip()
    created_by = str(row.get("Created by", "")).strip()
    review_period = str(row.get("Review Period", "")).strip()
    purpose = str(row.get("Purpose", "")).strip()

    # === Determine subfolder ===
    if folder_type == "1. Handbook":
        section_category = section1
    elif folder_type == "2. Handbook Companion":
        section_category = section2  # 🔒 future expansion
    elif folder_type == "3. Project Specific Processes":
        section_category = section3  # 🔒 future expansion
    elif folder_type == "4. Data Repository":
        section_category = section4  # 🔒 future expansion
    else:
        section_category = "Uncategorized"

    # === Construct folder and filename ===
    safe_title = process_title.replace("/", "-").replace(" ", "_")
    safe_number = process_number.replace("/", "-").replace(" ", "_")
    filename = f"{safe_number}_{safe_title}.md"

    folder_path = OUTPUT_DIR / section_category
    file_path = folder_path / filename
    folder_path.mkdir(parents=True, exist_ok=True)

    if file_path.exists():
        continue

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

    # === Save to file ===
    folder_path.mkdir(parents=True, exist_ok=True)
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(md)

    print(f"✅ Wrote: {file_path}")
