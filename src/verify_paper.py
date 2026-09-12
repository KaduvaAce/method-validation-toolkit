import pandas as pd

PAPER = "data/papers/mesalamine_2025_accuracy.csv"
TOLERANCE = 0.02  # percentage points; set by the paper's 2-dp reporting precision

data = pd.read_csv(PAPER)
data["my_recovery_pct"] = (data["found_mg"] / data["added_mg"]) * 100
data["difference"] = data["my_recovery_pct"] - data["paper_recovery_pct"]

print(f"Source: {PAPER}\n")
print("Level   Paper    Mine     Diff     Match")
for row in data.itertuples():
    match = "YES" if abs(row.difference) <= TOLERANCE else "NO"
    print(f"{row.level:>5}  {row.paper_recovery_pct:>6.2f}%  "
          f"{row.my_recovery_pct:>6.2f}%  {row.difference:>+6.3f}   {match}")

n_match = (data["difference"].abs() <= TOLERANCE).sum()
print(f"\n{n_match} of {len(data)} values reproduced within {TOLERANCE} points")