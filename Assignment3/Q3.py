# 3.Date Split
from sklearn.model_selection import train_test_split

# Define features and target
X = df.drop('Price', axis=1)
y = df['Price']

# Split the data into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Display the shapes of the splits
print("Training set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)
