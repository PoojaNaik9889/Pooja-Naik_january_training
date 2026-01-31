## 6. Interpretation and Conclusion
# Get the coefficients of the model
coefficients = pd.DataFrame(model.coef_, X.columns, columns=['Coefficient'])

# Display the coefficients
print("Model Coefficients:\n", coefficients)

# Interpret the relationship (example print statement)
print("\nInterpretation:")
print("Features with higher coefficients have a stronger impact on the house price.")



