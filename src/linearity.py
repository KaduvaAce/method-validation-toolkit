import pandas as pd
import numpy as np

data = pd.read_csv("data/example_calibration.csv")
x = data["concentration"].to_numpy()
y = data["peak_area"].to_numpy()

n = len(x)
x_mean = x.mean()
y_mean = y.mean()

slope = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
intercept = y_mean - slope * x_mean

predicted = slope * x + intercept
residuals = y - predicted

ss_res = (residuals ** 2).sum()
ss_tot = ((y - y_mean) ** 2).sum()
r_squared = 1 - ss_res / ss_tot

sigma = np.sqrt(ss_res / (n - 2))

print(f"Slope:      {slope:.2f}")
print(f"Intercept:  {intercept:.2f}")
print(f"R-squared:  {r_squared:.5f}")
print(f"Sigma:      {sigma:.2f}")
print(f"Residuals:  {np.round(residuals, 1)}")
lod = 3.3 * sigma / slope
loq = 10 * sigma / slope

print(f"LOD:        {lod:.3f} ug/mL")
print(f"LOQ:        {loq:.3f} ug/mL")