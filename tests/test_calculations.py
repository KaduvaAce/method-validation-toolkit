import numpy as np
import pandas as pd


def fit(x, y):
    """Least-squares fit. Returns slope, intercept, R-squared, residual SD."""
    n = len(x)
    x_mean, y_mean = x.mean(), y.mean()
    slope = ((x - x_mean) * (y - y_mean)).sum() / ((x - x_mean) ** 2).sum()
    intercept = y_mean - slope * x_mean
    residuals = y - (slope * x + intercept)
    ss_res = (residuals ** 2).sum()
    r_squared = 1 - ss_res / ((y - y_mean) ** 2).sum()
    return slope, intercept, r_squared, np.sqrt(ss_res / (n - 2))


def test_example_dataset():
    """Hand-checked values from the example calibration data."""
    data = pd.read_csv("data/example_calibration.csv")
    slope, intercept, r2, sigma = fit(
        data["concentration"].to_numpy(dtype=float),
        data["peak_area"].to_numpy(dtype=float),
    )
    assert round(slope, 2) == 100.10
    assert round(intercept, 2) == 17.00
    assert round(r2, 5) == 0.99970
    assert round(sigma, 2) == 31.57


def test_lod_loq_ratio():
    """LOQ must always be 10/3.3 times the LOD for any sigma and slope."""
    sigma, slope = 209.89, 417.125
    lod = 3.3 * sigma / slope
    loq = 10 * sigma / slope
    assert round(loq / lod, 4) == round(10 / 3.3, 4)


def test_mesalamine_regression_not_reproducible():
    """The published equation cannot be derived from the published table."""
    data = pd.read_csv("data/papers/mesalamine_2025_linearity.csv")
    slope, intercept, r2, _ = fit(
        data["concentration"].to_numpy(dtype=float),
        data["mean_peak_area"].to_numpy(dtype=float),
    )
    assert round(slope, 2) == 417.13
    assert round(intercept, 2) == 337.04
    assert abs(r2 - 0.9992) < 0.001
    assert abs(slope - 173.53) > 200