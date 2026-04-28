from sklearn.datasets import make_regression
import matplotlib.pyplot as plt
import numpy as np

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import Lasso

# data
X, y = make_regression(
    n_samples=100,
    n_features=1,
    n_informative=1,
    noise=20,
    random_state=13
)

# models
lr = LinearRegression()
lr.fit(X, y)

lasso1 = Lasso(alpha=1)
lasso1.fit(X, y)

lasso2 = Lasso(alpha=10)
lasso2.fit(X, y)

print("Linear:", lr.coef_, lr.intercept_)
print("Lasso 1:", lasso1.coef_, lasso1.intercept_)
print("Lasso 10:", lasso2.coef_, lasso2.intercept_)

# sort for smooth line
sort_idx = np.argsort(X[:, 0])
X_sorted = X[sort_idx]

# subplot
fig, axes = plt.subplots(1, 2, figsize=(18, 5))

# subplot 1 — original data
axes[0].scatter(X, y)
axes[0].set_title("Original Data")

# subplot 2 — Lasso comparison
axes[1].scatter(X, y, alpha=0.5)
axes[1].plot(X_sorted, lr.predict(X_sorted), color='red', label='Linear')
axes[1].plot(X_sorted, lasso1.predict(X_sorted), color='green', label='alpha=1')
axes[1].plot(X_sorted, lasso2.predict(X_sorted), color='orange', label='alpha=10')

axes[1].legend()
axes[1].set_title("Lasso Regression")

plt.tight_layout()
plt.savefig("lasso_comparison.png")
print("Saved as lasso_comparison.png")