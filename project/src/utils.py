# src/generate_churn_dataset.py

import pandas as pd
import numpy as np
from datetime import timedelta

def load_data(path):
    """Load the Online Retail dataset."""
    df = pd.read_excel(path)  # 数据集是 Excel 格式
    print("Raw shape:", df.shape)
    return df

def clean_data(df):
    """Remove invalid rows."""
    # 去掉 CustomerID 缺失的行
    df = df.dropna(subset=['CustomerID'])
    # 去掉退货 (Quantity < 0)
    df = df[df['Quantity'] > 0]
    # 转换日期格式
    df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])
    return df

def create_rfm(df, cutoff_date, window=60):
    """Generate RFM features for each customer in observation window."""
    start_date = cutoff_date - timedelta(days=window)
    mask = (df['InvoiceDate'] >= start_date) & (df['InvoiceDate'] <= cutoff_date)
    df_window = df.loc[mask]

    rfm = df_window.groupby('CustomerID').agg({
        'InvoiceDate': lambda x: (cutoff_date - x.max()).days,  # Recency
        'InvoiceNo': 'count',  # Frequency
        'Quantity': 'sum'      # Monetary proxy (数量，也可以用金额)
    }).reset_index()

    rfm.columns = ['CustomerID', 'Recency', 'Frequency', 'Monetary']
    return rfm

def create_churn_label(df, cutoff_date, horizon=30):
    """Define churn label based on future purchase (prediction window)."""
    future_mask = (df['InvoiceDate'] > cutoff_date) & (df['InvoiceDate'] <= cutoff_date + timedelta(days=horizon))
    future = df.loc[future_mask]

    churn_users = set(r['CustomerID'] for _, r in future.iterrows())
    return churn_users

def generate_dataset(path, cutoff_date="2011-08-01"):
    """Pipeline to generate churn dataset."""
    df = load_data(path)
    df = clean_data(df)

    cutoff_date = pd.to_datetime(cutoff_date)

    # Step 1: create features
    rfm = create_rfm(df, cutoff_date)

    # Step 2: create churn labels
    future_users = create_churn_label(df, cutoff_date)
    rfm['churn'] = rfm['CustomerID'].apply(lambda x: 0 if x in future_users else 1)

    print("Final dataset shape:", rfm.shape)
    return rfm

if __name__ == "__main__":
    dataset = generate_dataset("../data/raw/OnlineRetail.xlsx")
    dataset.to_csv("../data/processed/churn_dataset.csv", index=False)
    print("Processed dataset saved to ../data/processed/churn_dataset.csv")
