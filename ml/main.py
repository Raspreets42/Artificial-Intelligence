# from sklearn.linear_model import LinearRegression
#
# # Data (experience vs salary)
# X = [[1], [2], [3], [4]]
# y = [30000, 50000, 70000, 90000]
#
# model = LinearRegression()
# model.fit(X, y)
#
# # Prediction
# print(model.predict([[5]]))  # Predict salary for 5 years experience

# ---------------------------------------------------------------------------

# Using partial_fit (online learning style)
from sklearn.linear_model import SGDRegressor

model = SGDRegressor()

# First batch
model.partial_fit([[1], [2], [3]], [10, 20, 30])

# New data comes later
model.partial_fit([[4]], [40])

print(model.predict([[5]]))