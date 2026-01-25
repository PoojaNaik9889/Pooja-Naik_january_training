#Feature scaling is used to normalize numerical features so that they contribute equally to the model. Min-Max Scaling scales values between 0 and 1. Max Absolute Scaling scales values between −1 and 1. Vector Normalization scales data based on vector magnitude. Z-score standardization transforms features to have zero mean and unit variance. Feature scaling improves convergence speed and accuracy of machine learning models.
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, MaxAbsScaler, Normalizer, StandardScaler

df = pd.read_csv("train.csv")

num_cols = ["Age", "Fare"]

# Fill missing values first
df["Age"].fillna(df["Age"].median(), inplace=True)
df["Fare"].fillna(df["Fare"].median(), inplace=True)

# -----------------------------
# MIN-MAX SCALING
# -----------------------------
minmax = MinMaxScaler()
df[num_cols] = minmax.fit_transform(df[num_cols])
print("Min-Max Scaling done")

# -----------------------------
# MAX ABSOLUTE SCALING
# -----------------------------
maxabs = MaxAbsScaler()
df[num_cols] = maxabs.fit_transform(df[num_cols])
print("MaxAbs Scaling done")

# -----------------------------
# VECTOR NORMALIZATION
# -----------------------------
normalizer = Normalizer()
df[num_cols] = normalizer.fit_transform(df[num_cols])
print("Vector Normalization done")

# -----------------------------
# Z-SCORE STANDARDIZATION
# -----------------------------
standard = StandardScaler()
df[num_cols] = standard.fit_transform(df[num_cols])
print("Z-score Standardization done")

print(df.head())
