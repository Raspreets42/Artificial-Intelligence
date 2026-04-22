import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Create a sample dataset (e.g., sales data)
np.random.seed(42)
data = {
    'Revenue': np.random.normal(500, 100, 100),
    'Marketing_Spend': np.random.normal(100, 30, 100),
    'Customers': np.random.poisson(200, 100),
    'Returns': np.random.normal(20, 5, 100),
    'Discount': np.random.uniform(0, 0.2, 100)
}
df = pd.DataFrame(data)

# Compute correlation matrix
corr_matrix = df.corr()

# Plot heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix,
            annot=True,          # show correlation values
            cmap='coolwarm',     # color scheme
            vmin=-1, vmax=1,     # correlation range
            square=True,         # square cells
            fmt='.2f',           # 2 decimal places
            linewidths=0.5)      # grid lines

plt.title('Correlation Matrix Heatmap')
plt.tight_layout()
plt.show()