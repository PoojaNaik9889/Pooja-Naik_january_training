#Train-test splitting is used to evaluate model performance on unseen data by dividing the dataset into training and testing sets. Skewed numerical features such as Fare are transformed using logarithmic transformation to reduce skewness and improve data distribution. These additional steps improve model generalization, stability, and predictive accuracy.
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

df = pd.read_csv("train.csv")

# -----------------------------
# TRAIN-TEST SPLIT
# -----------------------------
X = df.drop("Survived", axis=1)
y = df["Survived"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("Train-Test Split completed")

# -----------------------------
# SKEWED FEATURE TRANSFORMATION
# -----------------------------
df["Fare_Log"] = np.log1p(df["Fare"])

print("Log transformation applied on Fare")
print(df[["Fare", "Fare_Log"]].head())
