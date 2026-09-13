import numpy as np
import pandas as pd
import yaml

PAPER = "data/papers/mesalamine_2025_linearity.csv"
CONFIG = "config/limits.yaml"

PUBLISHED = {
    "slope": 173.53,
    "intercept": -2435.64,
    "r_squared": 0.9992,
    "lod": 0.22,
    "loq": 0.68,
}

with open(CONFIG) as f:
    cfg = yaml.safe_load(f)

sens = cfg["sensitivity"]
method = sens["sigma_method"]

data = pd.read_csv(PAPER)
x = data["concentration"].to_numpy(dtype=float)
y = data["mean_peak_area"].to_numpy(dtype=float)

n = len(x)
x_mean, y_mean = x.mean(), y.mean()
sxx = ((x - x_mean) ** 2).sum()

slope = ((x - x_mean) * (y - y_mean)).sum() / sxx
intercept = y_mean - slope * x_mean
residuals = y - (slope * x + intercept)

ss_res = (residuals ** 2).sum()
r_squared = 1 - ss_res / ((y - y_mean) ** 2).sum()
residual_sd = np.sqrt(ss_res / (n - 2))

if method == "residual":
    sigma = residual_sd
elif method == "intercept_se":
    sigma = residual_sd * np.sqrt(1 / n + x_mean ** 2 / sxx)
else:
    raise ValueError(f"Unknown sigma_method: {method}")

mine = {
    "slope": slope,
    "intercept": intercept,
    "r_squared": r_squared,
    "lod": sens["lod_factor"] * sigma / slope,
    "loq": sens["loq_factor"] * sigma / slope,
}

print(f"Source: {PAPER}")
print(f"n = {n}   sigma method: {method}   sigma = {sigma:.2f}\n")
print("Parameter    Published        Mine      Difference   Ratio")
for key, published in PUBLISHED.items():
    diff = mine[key] - published
    ratio = mine[key] / published if published else float("nan")
    print(f"{key:<11} {published:>10.4f}  {mine[key]:>10.4f}  "
          f"{diff:>+11.4f}  {ratio:>6.2f}")

verdict = "PASS" if r_squared >= cfg["linearity"]["r_squared_min"] else "FAIL"
print(f"\nLinearity: {verdict} (R2 limit {cfg['linearity']['r_squared_min']})")