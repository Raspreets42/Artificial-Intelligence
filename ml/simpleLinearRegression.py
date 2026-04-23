import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, root_mean_squared_error, r2_score, adjusted_rand_score

df = pd.read_csv('placement.csv')

print(df.head())

x = df.iloc[:, 0:1]
y = df.iloc[:, -1]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=2)
lr = LinearRegression()
lr.fit(x_train, y_train)


plt.scatter(df['cgpa'], df['package'])
plt.plot(x_train, lr.predict(x_train), color='red')
plt.xlabel('CGPA')
plt.ylabel('Package')
plt.title('CGPA vs Package')
plt.savefig("plot.png")
print("Plot saved as plot.png")

y_pred = lr.predict(x_test)
y_pred = pd.Series(y_pred, index=y_test.index)
print("Predicted values:", y_pred)

slope = lr.coef_
intercept = lr.intercept_
print(f"Slope: {slope}, intercept: {intercept}")

print(f"check for x_test[0] ({x_test.values[0]})", slope * x_test.values[0] + intercept)

mse = mean_squared_error(y_test, y_pred)
print("Mean Squared Error:", mse)

mae = mean_absolute_error(y_test, y_pred)
print("Mean Absolute Error:", mae)

rmse = np.sqrt(mse)
print("Root Mean Squared Error:", rmse)

r2Score = r2_score(y_test, y_pred)
print("r2Score:", r2Score)

adjustedR2Score = 1 - (1 - r2Score) * (len(y_test) - 1) / (len(y_test) - x_test.shape[1] - 1)
print("Adjusted R2 Score:", adjustedR2Score)