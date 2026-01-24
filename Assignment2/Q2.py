# ======================================
# Assignment 2
# Question 2: Data Preprocessing
# ======================================

import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("train.csv")

# -------------------------------
# 1. Handling missing values
# -------------------------------
numeric_cols = df.select_dtypes(include=np.number).columns
df[numeric_cols] = df[numeric_cols].fillna(df[numeric_cols].median())

categorical_cols = df.select_dtypes(include='object').columns
for col in categorical_cols:
    df[col].fillna(df[col].mode()[0], inplace=True)

# -------------------------------
# 2. Fixing incorrect data types
# -------------------------------
for col in numeric_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# -------------------------------
# 3. Removing duplicate records
# -------------------------------
df.drop_duplicates(inplace=True)

# -------------------------------
# 4. Detecting and treating outliers (IQR)
# -------------------------------
for col in numeric_cols:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR
    df[col] = np.where(df[col] < lower, lower,
                       np.where(df[col] > upper, upper, df[col]))

# -------------------------------
# 5. Dropping irrelevant features
# -------------------------------
irrelevant_cols = ['PassengerId']
df.drop(columns=[c for c in irrelevant_cols if c in df.columns],
        inplace=True)

# Save cleaned dataset
df.to_csv("cleaned_train.csv", index=False)

print("Data preprocessing completed successfully")