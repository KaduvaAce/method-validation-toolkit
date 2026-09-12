import pandas as pd

data = pd.read_csv("data/example_accuracy.csv")
data["recovery"] = (data["found_ugml"] / data["added_ugml"]) * 100

print("Level  Mean recovery   %RSD    Verdict")
for level, group in data.groupby("level"):
    mean_rec = group["recovery"].mean()
    rsd = (group["recovery"].std(ddof=1) / mean_rec) * 100
    ok = 98.0 <= mean_rec <= 102.0
    print(f"{level:>5}  {mean_rec:>11.2f}%  {rsd:>5.2f}%   {'PASS' if ok else 'FAIL'}")

overall = data["recovery"].mean()
print(f"\nOverall mean recovery: {overall:.2f}% (limit 98-102%)")