import numpy as np
import pandas as pd
import plotly.express as px

# for reproducibility
np.random.seed(23)

# -----------------------------
# Class 1 (target = 1)
# -----------------------------
mu_vec1 = np.array([0, 0, 0])

cov_mat1 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

class1_sample = np.random.multivariate_normal(
    mu_vec1,
    cov_mat1,
    20
)

df1 = pd.DataFrame(
    class1_sample,
    columns=['feature1', 'feature2', 'feature3']
)

df1['target'] = 1


# -----------------------------
# Class 2 (target = 0)
# -----------------------------
mu_vec2 = np.array([1, 1, 1])

cov_mat2 = np.array([
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

class2_sample = np.random.multivariate_normal(
    mu_vec2,
    cov_mat2,
    20
)

df2 = pd.DataFrame(
    class2_sample,
    columns=['feature1', 'feature2', 'feature3']
)

df2['target'] = 0

df = pd.concat([df1, df2], ignore_index=True)

print(df.sample(5))
print("\nShape:", df.shape)

# fig = px.scatter_3d(df, x=df['feature1'], y=df['feature2'], z=df['feature3'], color=df['target'].astype('str'))
# fig.update_traces(marker=dict(size=12, line=dict(width=2, color='DarkSlateGrey')), selector=dict(mode='markers'))
# fig.show()


# Step 1: Apply standard scaling
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

df.iloc[:, 0:3] = scaler.fit_transform(df.iloc[:, 0:3])
print("scaled df :: ", df.iloc[:, 0:3])

# Step 2: Find the covariance Matrix
covMatrix = np.cov([df.iloc[:, 0], df.iloc[:, 1], df.iloc[:, 2]])
print("covMatrix :: ", covMatrix)

# Step 3: Find EigenVectors and EigenValues
eval, evec = np.linalg.eig(covMatrix)
print("EigenVectors :: ", evec)
print("EigenValues :: ", eval)

# Optional
import plotly.graph_objects as go
origin = [0, 0, 0]
fig = go.Figure()
# plot eigenvectors
for i in range(3):
    fig.add_trace(go.Scatter3d(
        x=[origin[0], evec[0, i]],
        y=[origin[1], evec[1, i]],
        z=[origin[2], evec[2, i]],
        mode='lines+markers',
        line=dict(width=6),
        name=f"EigenVector {i+1}"
    ))
fig.update_layout(
    title="Eigenvectors Visualization",
    scene=dict(
        xaxis_title='feature1',
        yaxis_title='feature2',
        zaxis_title='feature3'
    )
)
fig.show()


# Step 4: Sort Eigenvalues & Eigenvectors (descending order)
idx = np.argsort(eval)[::-1]

eval_sorted = eval[idx]
evec_sorted = evec[:, idx]
print("Sorted EigenValues:\n", eval_sorted)
print("Sorted EigenVectors:\n", evec_sorted)

# Step 5: Select top-k components
k = 2   # choose number of principal components

top_k_eigenvalues = eval_sorted[:k]
top_k_eigenvectors = evec_sorted[0:k]

print("\nTop K EigenValues:\n", top_k_eigenvalues)
print("\nTop K EigenVectors:\n", top_k_eigenvectors)

# step 6: Transform data
transformedDf = np.dot(df.iloc[:, 0:3], top_k_eigenvectors.T)
print("transformedDf :: ", transformedDf)
newDf = pd.DataFrame(transformedDf, columns=['PC1', 'PC2'])
newDf['target'] = df['target'].values

print(newDf.sample(5))