import matplotlib
matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

PAPER = "data/papers/mesalamine_2025_linearity.csv"
OUTPUT = "reports/mesalamine_residuals.png"

data = pd.read_csv(PAPER)
x = data["concentration"].to_numpy(dtype=float)
y = data["mean_peak_area"].to_numpy(dtype=float)

x_mean, y_mean = x.mean(), y.mean()
slope = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
intercept = y_mean - slope * x_mean
residuals = y - (slope * x + intercept)

fig, (top, bottom) = plt.subplots(2, 1, figsize=(7, 8))

top.scatter(x, y, color="navy", zorder=3)
top.plot(x, slope * x + intercept, color="crimson", linestyle="--")
top.set_xlabel("Concentration (ug/mL)")
top.set_ylabel("Mean peak area")
top.set_title(f"y = {slope:.2f}x + {intercept:.2f}")
top.grid(alpha=0.3)

bottom.axhline(0, color="grey", linewidth=1)
bottom.scatter(x, residuals, color="navy", zorder=3)
bottom.set_xlabel("Concentration (ug/mL)")
bottom.set_ylabel("Residual (area units)")
bottom.set_title("Residuals")
bottom.grid(alpha=0.3)

fig.tight_layout()
fig.savefig(OUTPUT, dpi=150)
print(f"Saved {OUTPUT}")
print(f"Residuals: {np.round(residuals, 1)}")