#!/usr/bin/env python3
import csv
import os
from pathlib import Path

"""ETL Demo Script
A lightweight Extract-Transform-Load demonstration aligned with the README's ETL concepts.
- Extract: read from data/input.csv (creates a sample if missing)
- Transform: uppercase/title-case names and ensure numeric values
- Load: write results to data/output.csv
"""

def ensure_dirs():
    Path("data").mkdir(exist_ok=True)


def create_sample_csv(path: str = "data/input.csv"):
    ensure_dirs()
    with open(path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "value"])
        writer.writerow([1, "alice", 23])
        writer.writerow([2, "bob", 67])
        writer.writerow([3, "carol", 45])
        writer.writerow([4, "dave", 92])


def extract(input_path: str = "data/input.csv"):
    data = []
    with open(input_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append({"id": int(row["id"]), "name": row["name"], "value": int(row["value"])})
    return data


def transform(records):
    # Example transformations: title-case names and ensure numeric types
    for r in records:
        r["name"] = r["name"].title()
        r["value"] = int(r["value"])
    return records


def load(records, output_path: str = "data/output.csv"):
    fieldnames = ["id", "name", "value"]
    with open(output_path, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for r in records:
            writer.writerow({"id": r["id"], "name": r["name"], "value": r["value"]})


def etl_pipeline():
    if not os.path.exists("data/input.csv"):
        create_sample_csv("data/input.csv")
        print("Created sample input at data/input.csv")
    data = extract("data/input.csv")
    data = transform(data)
    load(data, "data/output.csv")
    print(f"ETL complete. Output written to data/output.csv with {len(data)} records.")


if __name__ == "__main__":
    etl_pipeline()
