import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score
def detect_outliers_iqr(series: pd.Series, k: float = 1.5) -> pd.Series:
    """Return boolean mask for IQR-based outliers.
    Detect outliers in a numeric pandas Series using the IQR method.
    
    Parameters
    ----------
    series : pd.Series
        Input numeric data.
    
    Returns
    -------
    pd.Series
        Boolean Series: True if the observation is an outlier, False otherwise.
    Assumptions: distribution reasonably summarized by quartiles; k controls strictness.
    """
    q1 = series.quantile(0.25)
    q3 = series.quantile(0.75)
    iqr = q3 - q1
    lower = q1 - k * iqr
    upper = q3 + k * iqr
    return (series < lower) | (series > upper)

def detect_outliers_zscore(series: pd.Series, threshold: float = 3.0) -> pd.Series:
    """Return boolean mask for Z-score outliers where |z| > threshold.
     Detect outliers in a numeric pandas Series using Z-score method.
    
    Parameters
    ----------
    series : pd.Series
        Input numeric data.
    threshold : float, default=3.0
        Z-score cutoff beyond which values are flagged as outliers.
    
    Returns
    -------
    pd.Series
        Boolean Series: True if outlier, False otherwise.
    Assumptions: roughly normal distribution; sensitive to heavy tails.
    """
    mu = series.mean()
    sigma = series.std(ddof=0)
    z = (series - mu) / (sigma if sigma != 0 else 1.0)
    return z.abs() > threshold

def winsorize_series(series: pd.Series, lower: float = 0.05, upper: float = 0.95) -> pd.Series:
    """
    Winsorize a pandas Series by capping extreme values.
    
    Parameters
    ----------
    series : pd.Series
        Input numeric data.
    lower : float, default=0.05
        Lower quantile cutoff (e.g., 0.05 keeps the bottom 5% capped).
    upper : float, default=0.95
        Upper quantile cutoff.
    
    Returns
    -------
    pd.Series
        Winsorized series.
    """
    lo = series.quantile(lower)
    hi = series.quantile(upper)
    return series.clip(lower=lo, upper=hi)