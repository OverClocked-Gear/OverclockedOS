from pathlib import Path
import csv

ROOT = Path(r"research_corpus\Kinetic Economy")
INV = ROOT / "_inventory"
ROLE_AUDIT = INV / "file_role_audit.csv"
OUT_CSV = INV / "source_document_manifest.csv"
OUT_MD = INV / "source_document_summary.md"

SOURCE_ROLES = {"source_document"}

rows = []

with open(ROLE_AUDIT, newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["file_role"] in SOURCE_ROLES:
            rows.append(row)

if not rows:
    raise ValueError("No source documents found.")

# Reassign stable source ids for source documents only
for i, row in enumerate(rows, start=1):
    row["source_doc_id"] = f"codex_doc_{i:06d}"

fieldnames = ["source_doc_id"] + [c for c in rows[0].keys() if c != "source_doc_id"]

with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

type_counts = {}
for row in rows:
    ft = row["file_type"] or "no_extension"
    type_counts[ft] = type_counts.get(ft, 0) + 1

with open(OUT_MD, "w", encoding="utf-8") as f:
    f.write("# Source Document Manifest Summary\n\n")
    f.write(f"Source documents: {len(rows)}\n\n")
    f.write("## Source Document Types\n\n")
    for file_type, count in sorted(type_counts.items()):
        f.write(f"- {file_type}: {count}\n")

print(f"Source document manifest written to: {OUT_CSV}")
print(f"Summary written to: {OUT_MD}")
