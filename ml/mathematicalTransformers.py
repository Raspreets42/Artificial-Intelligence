import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

loaded = [
    {"id": 1, "value": 2.5},
    {"id": 2, "value": 1.2},
    {"id": 3, "value": 8.7},
    {"id": 4, "value": 0.3},
    {"id": 5, "value": 5.1},
    {"id": 6, "value": 15.0},
    {"id": 7, "value": 0.9},
    {"id": 8, "value": 4.4},
    {"id": 9, "value": 12.3},
    {"id": 10, "value": 0.05},
    {"id": 11, "value": 6.8},
    {"id": 12, "value": 20.0},
]

values = np.array([d["value"] for d in loaded])
print(f"\nOriginal values:\n{values}")

# ------------------------------------------------------------
# 1. Define transformations (with safety for edge cases)
# ------------------------------------------------------------

# Log transform: use log1p to handle zeros (log(1+x))
values_log = np.log1p(values)          # safe for x >= 0

# Square transform
values_square = values ** 2

# Square root transform (safe for non‑negative)
values_sqrt = np.sqrt(values)

# Reciprocal transform: add small epsilon to avoid division by zero
epsilon = 1e-6
values_recip = 1.0 / (values + epsilon)

# ------------------------------------------------------------
# 2. Create Q‑Q plots for each transformed variable
#    (compares distribution to a theoretical normal)
# ------------------------------------------------------------
transformations = {
    "Original (no transform)": values,
    "Log (log1p)": values_log,
    "Square": values_square,
    "Square root": values_sqrt,
    "Reciprocal (1/(x+ε))": values_recip,
}

fig, axes = plt.subplots(2, 3, figsize=(15, 10))
axes = axes.flatten()

for idx, (name, data) in enumerate(transformations.items()):
    ax = axes[idx]
    stats.probplot(data, dist="norm", plot=ax)
    ax.set_title(f"Q-Q Plot: {name}")
    ax.grid(True, alpha=0.3)

# Hide the unused subplot if any (we have 5 transforms, 6 axes)
axes[5].axis("off")

plt.tight_layout()
plt.show()

# ------------------------------------------------------------
# 3. Demonstrate use in a Pipeline (e.g., with LinearRegression)
#    This part shows how to embed a transformer in sklearn
# ------------------------------------------------------------
from sklearn.preprocessing import FunctionTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Create a synthetic target (just for demonstration)
np.random.seed(42)
y = 2.5 * values + np.random.normal(0, 1, size=len(values))

X = values.reshape(-1, 1)   # feature as column

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Pipeline with log transform (you can replace with any of the above)
pipe = Pipeline([
    ("log_transform", FunctionTransformer(np.log1p, validate=True)),
    ("regressor", LinearRegression())
])

pipe.fit(X_train, y_train)
score = pipe.score(X_test, y_test)
print(f"\nPipeline (log transform + LinearRegression) R² score: {score:.4f}")