# ======================================
# Assignment 2
# Question 1: Dataset Selection
# ======================================

import pandas as pd

# Dataset selected from Kaggle (Titanic dataset)
df = pd.read_csv("train.csv")

print("Dataset loaded successfully")
print(df.head())
print(df.info())
