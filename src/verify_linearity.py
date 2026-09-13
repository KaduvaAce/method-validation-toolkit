import pandas as pd
import numpy as np

PAPER = "data/papers/mesalamine_2025_linearity.csv"

PUBLISHED = {
    "slope": 173.53,
    "intercept": -2435.64,
    "r_squared": 0.9992,
    "lod": 0.22,
    "loq": 0.68,
}

data = pd.read_csv(PAPER)
x = data["concentration"].to_numpy(dtype=float)
y = data["mean_peak_area"].to_numpy(dtype=float)

n = len(x)
x_mean, y_mean = x.mean(), y.mean()

slope = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
intercept = y_mean - slope * x_mean
residuals = y - (slope * x + intercept)

ss_res = (residuals ** 2).sum()
ss_tot = ((y - y_mean) ** 2).sum()
r_squared = 1 - ss_res / ss_tot
sigma = np.sqrt(ss_res / (n - 2))

mine = {
    "slope": slope,
    "intercept": intercept,
    "r_squared": r_squared,
    "lod": 3.3 * sigma / slope,
    "loq": 10 * sigma / slope,
}

print(f"Source: {PAPER}   n = {n}\n")
print("Parameter    Published        Mine      Difference")
for key, published in PUBLISHED.items():
    diff = mine[key] - published
    print(f"{key:<11} {published:>10.4f}  {mine[key]:>10.4f}  {diff:>+12.4f}")

print(f"\nResidual SD (sigma): {sigma:.2f}")
print(f"Residuals: {np.round(residuals, 1)}")