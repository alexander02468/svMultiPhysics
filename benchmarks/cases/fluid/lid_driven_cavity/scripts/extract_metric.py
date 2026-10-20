
import argparse
import csv
import math
import sys
from pathlib import Path


def extract_metric(path: Path, reynolds: int, metric: str) -> float:
    with path.open(newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f)

        if reader.fieldnames is None or "reynolds" not in reader.fieldnames:
            raise ValueError("CSV missing 'reynolds' column")

        if metric not in reader.fieldnames:
            raise ValueError(f"CSV missing metric '{metric}'")

        matches = [
            row for row in reader
            if int(row["reynolds"]) == reynolds
        ]

    if len(matches) != 1:
        raise ValueError(
            f"Expected one row for Re={reynolds}, found {len(matches)}"
        )

    value = float(matches[0][metric])

    if not math.isfinite(value):
        raise ValueError(f"Non-finite value for '{metric}'")

    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", type=Path)
    parser.add_argument("reynolds", type=float)
    parser.add_argument("metric", type=str)
    args = parser.parse_args()

    try:
        value = extract_metric(
            args.csv_path, args.reynolds, args.metric
        )
    except (OSError, ValueError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        sys.exit(1)

    print(value)
