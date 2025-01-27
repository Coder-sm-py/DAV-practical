from sklearn import linear_model  # Corrected the import statement for scikit-learn

linreg = linear_model.LinearRegression()

# Use the linear regression model to fit the data
X = [[0, 0], [2, 2], [4, 4]]  # 2D input data
y = [0, 2, 4]  # Target values

# Fitting the model
linreg.fit(X, y)

# Print the coefficients
print(linreg.coef_)