from __future__ import annotations

import csv
from pathlib import Path


MIL_TO_MM = 0.0254
ROOT_DIR = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT_DIR / "datasheet" / "Tang_Primer_25K_52300_Pin_Length_table.csv"
OUTPUT_PATH = ROOT_DIR / "doc" / "Tang_Primer_25K_52300_Pin_Length_table.csv"


def clean_text(value: str) -> str:
    return value.strip().strip('"')


def read_normalized_rows() -> list[dict[str, str]]:
    normalized_rows: list[dict[str, str]] = []
    current_group = ""
    current_group_constraint = ""

    with SOURCE_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if not row:
                continue

            row_type = clean_text(row[0])
            if row_type == "Diff Pair:":
                current_group = clean_text(row[1]) if len(row) > 1 else ""
                current_group_constraint = clean_text(row[2]) if len(row) > 2 else ""
                continue

            if row_type != "Net:":
                continue

            key = clean_text(row[1]) if len(row) > 1 else ""
            if not key:
                continue

            electrical_constraint_set = clean_text(row[2]) if len(row) > 2 else ""
            length_mil_text = clean_text(row[11]) if len(row) > 11 else ""
            delay_ns_text = clean_text(row[12]) if len(row) > 12 else ""

            length_mil = float(length_mil_text) if length_mil_text else None
            length_mm = length_mil * MIL_TO_MM if length_mil is not None else None

            normalized_rows.append(
                {
                    "key": key,
                    "group_name": current_group,
                    "group_constraint_set": current_group_constraint,
                    "electrical_constraint_set": electrical_constraint_set,
                    "length_mil": "" if length_mil is None else f"{length_mil:.1f}",
                    "length_mm": "" if length_mm is None else f"{length_mm:.4f}",
                    "delay_ns": delay_ns_text,
                }
            )

    return normalized_rows


def main() -> None:
    rows = read_normalized_rows()
    with OUTPUT_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "key",
                "group_name",
                "group_constraint_set",
                "electrical_constraint_set",
                "length_mil",
                "length_mm",
                "delay_ns",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)

    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()