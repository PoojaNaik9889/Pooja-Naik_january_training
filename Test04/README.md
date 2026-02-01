# Test04 – Supervised Machine Learning Models for House Price Prediction

## Problem Statement
The objective of this project is to evaluate the understanding of supervised machine learning concepts, data preprocessing techniques, and model building. The task involves predicting house prices using multiple supervised learning algorithms and comparing their performance.

## Dataset Description
The dataset used in this project is the California Housing dataset obtained from Kaggle. It contains housing-related attributes such as location, median income, total rooms, population, and ocean proximity.  
The target variable for prediction is **median_house_value**, which represents the median house price in a given area.

## Data Preprocessing Steps
Before applying machine learning algorithms, the dataset was cleaned and preprocessed as follows:
- Missing values in numerical columns were handled using the median.
- Missing values in categorical columns were handled using the mode.
- Duplicate records were identified and removed.
- Categorical variables were converted into numerical form using one-hot encoding.
- Outliers were detected and treated using the IQR (Interquartile Range) method on numerical features.
- Feature scaling was applied using StandardScaler to normalize the data.
- Irrelevant or redundant features were removed where necessary.
- The dataset was split into training (80%) and testing (20%) sets.

## Algorithms Used
The following supervised machine learning algorithms were implemented:
1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor
4. K-Nearest Neighbors (KNN)
5. Support Vector Machine (SVM)

## Evaluation Metrics and Results
Since this is a regression problem, the models were evaluated using the following metrics:
- R² Score
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- Mean Absolute Error (MAE)

The performance of all five models was compared based on these metrics.

## Conclusion / Observations
Among all the models, the Random Forest Regressor achieved the best performance with the highest R² score and lowest error values. This project demonstrates the importance of proper data preprocessing and shows how different supervised learning algorithms perform on the same dataset.

