import pandas as pd

PAPER = "data/papers/dihydropyridines_2025_accuracy.csv"
LABEL_COL = "drug"
ADDED_COL = "added_ugml"
FOUND_COL = "found_ugml"

ROUNDING_UNIT = 0.005  # half of the last reported decimal place

data = pd.read_csv(PAPER)
data["my_recovery_pct"] = (data[FOUND_COL] / data[ADDED_COL]) * 100
data["difference"] = data["my_recovery_pct"] - data["paper_recovery_pct"]
data["tolerance"] = (ROUNDING_UNIT / data[ADDED_COL]) * 100 + 0.005

print(f"Source: {PAPER}\n")
print("Item     Added   Paper     Mine      Diff    Tol     Match")
for row in data.itertuples():
    match = "YES" if abs(row.difference) <= row.tolerance else "NO"
    print(f"{getattr(row, LABEL_COL):<6} {getattr(row, ADDED_COL):>7.1f} "
          f"{row.paper_recovery_pct:>7.2f}% {row.my_recovery_pct:>7.2f}% "
          f"{row.difference:>+7.3f}  {row.tolerance:>5.3f}   {match}")

n_match = (data["difference"].abs() <= data["tolerance"]).sum()
print(f"\n{n_match} of {len(data)} values reproduced within rounding tolerance")