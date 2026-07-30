import csv

with open("sales.csv", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    rows = list(reader)
    fieldnames = reader.fieldnames + ["revenue"]

for r in rows:
    r["revenue"] = round(int(r["units"]) * float(r["unit_price"]), 2)

with open("report.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(rows)

print(f"report.csv zapisany, {len(rows)} riadkov")