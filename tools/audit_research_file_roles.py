from pathlib import Path
import csv

ROOT = Path(r"research_corpus\Kinetic Economy")
INV = ROOT / "_inventory"
MANIFEST = INV / "research_manifest.csv"
OUT_CSV = INV / "file_role_audit.csv"
OUT_MD = INV / "file_role_summary.md"

ROLE_MAP = {
    "pdf": "source_document",
    "docx": "source_document",
    "xlsx": "source_document",
    "csv": "data_table",
    "json": "parsed_extraction",
    "jsonl": "parsed_extraction",
    "md": "synthesis_note",
    "txt": "synthesis_note",
    "png": "image_asset",
    "jpg": "image_asset",
    "jpeg": "image_asset",
    "py": "script_or_log",
    "log": "script_or_log",
    "yaml": "metadata_or_config",
    "yml": "metadata_or_config",
    "": "unknown",
}

rows = []

if not MANIFEST.exists():
    raise FileNotFoundError(f"Manifest not found: {MANIFEST}")

with open(MANIFEST, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        file_type = row["file_type"].lower().strip()
        row["file_role"] = ROLE_MAP.get(file_type, "unknown")
        rows.append(row)

if not rows:
    raise ValueError("No rows found in manifest.")

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=rows[0].keys())
    writer.writeheader()
    writer.writerows(rows)

role_counts = {}
unknowns = []

for row in rows:
    role = row["file_role"]
    role_counts[role] = role_counts.get(role, 0) + 1
    if role == "unknown":
        unknowns.append(row)

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("# Research File Role Audit\n\n")
    f.write(f"Total files audited: {len(rows)}\n\n")

    f.write("## File Roles\n\n")
    for role, count in sorted(role_counts.items()):
        f.write(f"- {role}: {count}\n")

    f.write("\n## Unknown File Types\n\n")
    if unknowns:
        for row in unknowns:
            f.write(f"- {row['relative_path']} ({row['file_type']})\n")
    else:
        f.write("None.\n")

print(f"File role audit written to: {OUT_CSV}")
print(f"Summary written to: {OUT_MD}")
