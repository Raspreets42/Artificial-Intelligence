import pandas as pd
import numpy as np
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split


class RandomImputer(BaseEstimator, TransformerMixin):
    """Custom random imputer compatible with sklearn"""

    def __init__(self, random_state=None):
        self.random_state = random_state

    def fit(self, X, y=None):
        # Store non-missing values for each column
        self.non_missing_values_ = {}
        for col in X.columns:
            values = X[col].dropna().values
            if len(values) > 0:
                self.non_missing_values_[col] = values

        return self

    def transform(self, X):
        X_copy = X.copy()

        # Set random seed for reproducibility
        if self.random_state:
            np.random.seed(self.random_state)

        for col in X_copy.columns:
            if col in self.non_missing_values_ and X_copy[col].isna().any():
                non_missing = self.non_missing_values_[col]
                missing_mask = X_copy[col].isna()
                n_missing = missing_mask.sum()

                random_values = np.random.choice(
                    non_missing,
                    size=n_missing,
                    replace=True
                )
                X_copy.loc[missing_mask, col] = random_values

        return X_copy


# Usage in pipeline
df = pd.DataFrame({
    'feature1': [1, 2, np.nan, 4, 5],
    'feature2': [10, np.nan, 30, 40, 50],
    'target': [100, 200, 300, 400, 500]
})

X = df.drop('target', axis=1)
y = df['target']

pipeline = Pipeline([
    ('imputer', RandomImputer(random_state=42)),
    ('model', RandomForestRegressor())
])

pipeline.fit(X, y)
predictions = pipeline.predict(X)
print(predictions)