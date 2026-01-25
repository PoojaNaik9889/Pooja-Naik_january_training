## 6. Conclusion

This project implemented a complete data preprocessing pipeline on the Titanic dataset selected from Kaggle, following all required preprocessing steps.

For "missing value handling", the "median" method was most effective for numerical features such as 'Age' and 'Fare' because these features contained outliers and skewed distributions. Median imputation is robust to extreme values and preserved the original data characteristics. For categorical features such as 'Embarked', "mode imputation" worked best as it retained the most frequently occurring category without altering the categorical distribution.

In "categorical variable handling", different encoding techniques performed better for different feature types. "One-Hot Encoding" was most suitable for nominal features like 'Embarked' where no natural order exists. "Label Encoding" was effective for binary categorical features such as 'Sex'. "Ordinal Encoding" worked well for ordered features like 'Pclass'. "Frequency Encoding" captured the distribution of categorical values, while "Target Encoding" effectively represented the relationship between categorical variables and the target variable, making it useful for predictive modeling.

Among "feature scaling techniques", "Z-score standardization" was the most effective because it transformed numerical features to have zero mean and unit variance, which benefits many machine learning algorithms. Min-Max Scaling and Max Absolute Scaling were useful but sensitive to outliers, while Vector Normalization had limited impact for this dataset.

From "outlier analysis and skewness transformation", it was observed that features such as *Fare* were highly right-skewed. Instead of removing valid extreme values, "logarithmic transformation" was applied to reduce skewness and stabilize variance. This approach preserved important information while improving feature distribution.

Overall, the final preprocessing choices—median and mode imputation, feature-specific categorical encoding, Z-score standardization, and log transformation—resulted in a clean, well-structured dataset suitable for effective machine learning modeling and analysis.

