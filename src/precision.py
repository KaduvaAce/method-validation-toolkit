import pandas as pd
import numpy as np

data = pd.read_csv("data/example_precision.csv")
areas = data["peak_area"].to_numpy()

mean = areas.mean()
sd = areas.std(ddof=1)
rsd = (sd / mean) * 100

print(f"n:          {len(areas)}")
print(f"Mean:       {mean:.2f}")
print(f"SD:         {sd:.2f}")
print(f"%RSD:       {rsd:.3f}%")
print(f"Verdict:    {'PASS' if rsd <= 2.0 else 'FAIL'} (limit 2.0%)")