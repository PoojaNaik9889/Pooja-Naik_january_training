# 1.Data Cleaning
import pandas as pd

# Load the dataset
df = pd.read_csv('USA_Housing.csv')

# Check for missing values
missing_values = df.isnull().sum()

# Check for duplicate rows
duplicate_rows = df.duplicated().sum()

# Display results
print("Missing Values:\n", missing_values)
print("Duplicate Rows:", duplicate_rows)
