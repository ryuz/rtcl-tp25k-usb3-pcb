from __future__ import annotations

import csv
from pathlib import Path


MIL_TO_MM = 0.0254
ROOT_DIR = Path(__file__).resolve().parents[1]
PIN_ASSIGN_PATH = ROOT_DIR / "doc" / "pin_assign.csv"
SOM_LENGTH_PATH = ROOT_DIR / "datasheet" / "Tang_Primer_25K_52300_Pin_Length_table.csv"
PCB_LENGTH_PATH = ROOT_DIR / "rtcl-tp25k-usb3" / "lenth_table.csv"
OUTPUT_PATH = ROOT_DIR / "doc" / "pin_assign_with_lengths.csv"


def clean_text(value: str) -> str:
    return value.strip().strip('"')


def normalize_board_net_name(value: str) -> str:
    return clean_text(value).lstrip("/")


def normalize_som_datasheet_key(value: str) -> str:
    text = clean_text(value)
    if not text:
        return ""

    parts = [part for part in text.split("_") if part]
    if len(parts) >= 2:
        return parts[1]
    return text


def read_pin_assignments() -> list[dict[str, str]]:
    with PIN_ASSIGN_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        return [{key: clean_text(value) for key, value in row.items()} for row in reader]


def read_som_lengths_mm() -> dict[str, float]:
    lengths: dict[str, float] = {}
    with SOM_LENGTH_PATH.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.reader(handle)
        for row in reader:
            if not row or clean_text(row[0]) != "Net:":
                continue
            net_name = clean_text(row[1])
            if not net_name:
                continue
            length_mil = clean_text(row[11]) if len(row) > 11 else ""
            if not length_mil:
                continue
            lengths[net_name] = float(length_mil) * MIL_TO_MM
    return lengths


def read_pcb_lengths_mm() -> dict[str, float]:
    for encoding in ("cp932", "utf-8-sig", "utf-8"):
        try:
            with PCB_LENGTH_PATH.open("r", encoding=encoding, newline="") as handle:
                sample = handle.read(4096)
                handle.seek(0)

                try:
                    dialect = csv.Sniffer().sniff(sample, delimiters=",;")
                    delimiter = dialect.delimiter
                except csv.Error:
                    delimiter = ";" if sample.count(";") > sample.count(",") else ","

                reader = csv.reader(handle, delimiter=delimiter)
                next(reader, None)
                net_name_index = 0
                total_length_index = 2
                lengths: dict[str, float] = {}
                for row in reader:
                    if len(row) <= total_length_index:
                        continue
                    net_name = normalize_board_net_name(row[net_name_index])
                    length_text = clean_text(row[total_length_index])
                    if not net_name or not length_text:
                        continue
                    lengths[net_name] = float(length_text)
                return lengths
        except UnicodeDecodeError:
            continue

    raise UnicodeDecodeError("unknown", b"", 0, 1, "Unable to decode PCB length table")


def format_length(value: float | None) -> str:
    if value is None:
        return ""
    return f"{value:.4f}"


def main() -> None:
    pin_assignments = read_pin_assignments()
    som_lengths_mm = read_som_lengths_mm()
    pcb_lengths_mm = read_pcb_lengths_mm()

    output_rows: list[dict[str, str]] = []
    for row in pin_assignments:
        som_key = normalize_som_datasheet_key(row.get("SoMネット名", ""))
        som_inside_length = som_lengths_mm.get(som_key)
        board_som_length = pcb_lengths_mm.get(normalize_board_net_name(row.get("SoMネット名", "")))
        board_ft601_length = pcb_lengths_mm.get(normalize_board_net_name(row.get("FT601ネット名", "")))

        total_length = None
        if any(value is not None for value in (som_inside_length, board_som_length, board_ft601_length)):
            total_length = sum(value for value in (som_inside_length, board_som_length, board_ft601_length) if value is not None)

        output_row = dict(row)
        output_row["SoMデータシート照合キー"] = som_key
        output_row["SoM内配線長(mm)"] = format_length(som_inside_length)
        output_row["設計基板_SoM側配線長(mm)"] = format_length(board_som_length)
        output_row["設計基板_FT601側配線長(mm)"] = format_length(board_ft601_length)
        output_row["総配線長(mm)"] = format_length(total_length)
        output_rows.append(output_row)

    fieldnames = list(pin_assignments[0].keys()) + [
        "SoMデータシート照合キー",
        "SoM内配線長(mm)",
        "設計基板_SoM側配線長(mm)",
        "設計基板_FT601側配線長(mm)",
        "総配線長(mm)",
    ]
    with OUTPUT_PATH.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(output_rows)

    print(f"Wrote {OUTPUT_PATH}")


if __name__ == "__main__":
    main()