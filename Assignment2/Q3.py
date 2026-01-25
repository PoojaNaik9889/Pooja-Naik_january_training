#Categorical variables represent qualitative data and must be converted into numerical form before applying machine learning algorithms. Different encoding techniques are used based on the nature of the categorical feature. One-Hot Encoding creates binary columns for each category and is suitable for nominal variables. Label Encoding assigns unique integers to categories. Ordinal Encoding is used when categories have a meaningful order. Frequency Encoding replaces categories with their occurrence frequency. Target Encoding replaces categories with the mean of the target variable. Applying appropriate encoding techniques improves model performance and data representation.
import pandas as pd
from sklearn.preprocessing import LabelEncoder, OrdinalEncoder

# Load dataset
df = pd.read_csv("train.csv")

# -----------------------------
# ONE-HOT ENCODING
# -----------------------------
one_hot_df = pd.get_dummies(df, columns=["Embarked"])
print("One-Hot Encoding applied")

# -----------------------------
# LABEL ENCODING
# -----------------------------
le = LabelEncoder()
df["Sex_Label"] = le.fit_transform(df["Sex"])
print("Label Encoding applied")

# -----------------------------
# ORDINAL ENCODING
# (example using Pclass – ordered feature)
# -----------------------------
ordinal_encoder = OrdinalEncoder()
df["Pclass_Ordinal"] = ordinal_encoder.fit_transform(df[["Pclass"]])
print("Ordinal Encoding applied")

# -----------------------------
# FREQUENCY ENCODING
# -----------------------------
freq_map = df["Embarked"].value_counts() / len(df)
df["Embarked_Frequency"] = df["Embarked"].map(freq_map)
print("Frequency Encoding applied")

# -----------------------------
# TARGET ENCODING
# -----------------------------
target_mean = df.groupby("Sex")["Survived"].mean()
df["Sex_Target"] = df["Sex"].map(target_mean)
print("Target Encoding applied")

print(df.head())
