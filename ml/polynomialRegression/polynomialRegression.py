import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

# Sample dataset (non-linear)
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 5, 11, 19, 29])   # y = x^2

# -------------------------
# Linear Regression
# -------------------------
linear_model = LinearRegression()
linear_model.fit(X, y)

y_linear_pred = linear_model.predict(X)
linear_r2 = r2_score(y, y_linear_pred)

# -------------------------
# Polynomial Regression
# -------------------------
poly = PolynomialFeatures(degree=2)
X_poly = poly.fit_transform(X)

poly_model = LinearRegression()
poly_model.fit(X_poly, y)

y_poly_pred = poly_model.predict(X_poly)
poly_r2 = r2_score(y, y_poly_pred)


# -------------------------
# Print Results
# -------------------------
print("Linear R2 Score:", linear_r2)
print("Polynomial R2 Score:", poly_r2)

# -------------------------
# Plot
# -------------------------
plt.scatter(X, y, label="Actual Data")
plt.plot(X, y_linear_pred, label="Linear Regression")
plt.plot(X, y_poly_pred, label="Polynomial Regression")
plt.legend()
plt.title("Linear vs Polynomial Regression")
plt.savefig("plot.png")
print("Plot saved as plot.png")