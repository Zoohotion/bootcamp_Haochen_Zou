import pandas as pd
from sklearn.preprocessing import MinMaxScaler

def fill_missing_median(df: pd.DataFrame, columns=None):

    if columns is None:
        columns = df.select_dtypes(include="number").columns
    for col in columns:
        df[col] = df[col].fillna(df[col].median())
    return df

def drop_missing(df: pd.DataFrame, threshold=0.5):
   
    return df.dropna(thresh=int((1-threshold) * len(df)), axis=1)

def normalize_data(df: pd.DataFrame, columns=None):
   
    if columns is None:
        columns = df.select_dtypes(include="number").columns
    scaler = MinMaxScaler()
    df[columns] = scaler.fit_transform(df[columns])
    return df
