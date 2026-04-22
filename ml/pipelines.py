import json
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

sampleData = [
    {"age": 25, "income": 30000, "education_years": 12, "purchased": 0},
    {"age": 45, "income": 75000, "education_years": 16, "purchased": 1},
    {"age": 30, "income": 45000, "education_years": 14, "purchased": 0},
    {"age": 50, "income": 90000, "education_years": 18, "purchased": 1},
    {"age": 23, "income": 28000, "education_years": 12, "purchased": 0},
    {"age": 40, "income": 68000, "education_years": 15, "purchased": 1},
    {"age": 35, "income": 52000, "education_years": 13, "purchased": 0},
    {"age": 48, "income": 85000, "education_years": 17, "purchased": 1},
]

# Extract features and target
X = np.array([[d["age"], d["income"], d["education_years"]] for d in sampleData])
y = np.array([d["purchased"] for d in sampleData])

print("\nFeature matrix X:\n", X)
print("Target vector y:", y)

# 3. Split into training and test sets
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
print(f"\nTraining samples: {X_train}, Test samples: {X_test}")

# 4. Build and train the pipeline
pipe = Pipeline([
    ("scaler", StandardScaler()),   # Standardizes features (mean=0, std=1)
    ("model", LogisticRegression())
])

# Fit the pipeline on training data. This will:
#   - Call fit() on StandardScaler (computes mean and std of training features)
#   - Transform training features using those statistics
#   - Fit LogisticRegression on the scaled training features
pipe.fit(X_train, y_train)

# 5. Predict on test data
y_pred = pipe.predict(X_test)
print("\nTest set predictions:", y_pred)
print("True test labels:      ", y_test)

# Checking accuracy score
acc = accuracy_score(y_test, y_pred)
print("\nAccuracy:", acc)

# cross validation using pipeline
from sklearn.model_selection import cross_val_score
crossValScore = cross_val_score(pipe, X_train, y_train, cv=2, scoring='accuracy').mean()
print("crossValScore : ", crossValScore)