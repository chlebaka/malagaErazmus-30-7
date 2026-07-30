import csv
from collections import defaultdict

with open("sales.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

total = 0.0
per_product = defaultdict(float)

for r in rows:
    revenue = int(r["units"]) * float(r["unit_price"])
    total += revenue
    per_product[r["product"]] += revenue

print(f"Total revenue: {total:.2f}")
print("Top 3:")
for name, rev in sorted(per_product.items(), key=lambda x: -x[1])[:3]:
    print(f"  {name}: {rev:.2f}")