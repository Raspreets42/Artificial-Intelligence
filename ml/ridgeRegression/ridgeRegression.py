from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Ridge

# data
X, y = make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    n_targets=1,
    noise=20,
    random_state=13
)

# models
lr = LinearRegression()
lr.fit(X, y)

rr = Ridge(alpha=10)
rr.fit(X, y)

rr1 = Ridge(alpha=100)
rr1.fit(X, y)

print("Linear:", lr.coef_, lr.intercept_)
print("Ridge 10:", rr.coef_, rr.intercept_)
print("Ridge 100:", rr1.coef_, rr1.intercept_)

# sort X for smooth line
sort_idx = np.argsort(X[:, 0])
X_sorted = X[sort_idx]
y_sorted = y[sort_idx]

# create subplots
fig, axes = plt.subplots(1, 2, figsize=(18, 5))

# subplot 1 — scatter
axes[0].scatter(X, y)
axes[0].set_title("Original Data")

# subplot 2 — linear vs ridge
axes[1].scatter(X, y, alpha=0.5)
axes[1].plot(X_sorted, lr.predict(X_sorted), color='red', label='alpha=0')
axes[1].plot(X_sorted, rr.predict(X_sorted), color='green', label='alpha=10')
axes[1].plot(X_sorted, rr1.predict(X_sorted), color='orange', label='alpha=100')
axes[1].legend()
axes[1].set_title("Ridge vs Linear")

plt.tight_layout()
plt.savefig("ridge_comparison.png")
print("Saved as ridge_comparison.png")