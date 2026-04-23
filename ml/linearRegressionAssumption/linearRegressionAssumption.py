import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from statsmodels.stats.outliers_influence import variance_inflation_factor

df = pd.read_csv('data.csv')

X = df.iloc[:,0:3].values
y = df.iloc[:,-1].values

X_train,X_test,y_train,y_test = train_test_split(X,y,test_size=0.3,random_state=1)

model = LinearRegression()
model.fit(X_train,y_train)

# Residual
y_pred = model.predict(X_test)
residual = y_test - y_pred

vif = [] 
for i in range(X_train.shape[1]): 
    vif.append(variance_inflation_factor(X_train, i)) 

pd.DataFrame({'vif': vif}, index=df.columns[0:3]).T

# ===================== ONE FIGURE ======================
fig, axes = plt.subplots(3, 3, figsize=(16, 8))

# Feature scatter plots
axes[0,0].scatter(df['feature1'], df['target'])
axes[0,0].set_title("Feature1 vs Target")

axes[0,1].scatter(df['feature2'], df['target'])
axes[0,1].set_title("Feature2 vs Target")

axes[0,2].scatter(df['feature3'], df['target'])
axes[0,2].set_title("Feature3 vs Target")

# Correlation heatmap
sns.heatmap(df.iloc[:,0:3].corr(), annot=True, ax=axes[1,0])
axes[1,0].set_title("Correlation Heatmap")

# Normality of residual
sns.kdeplot(residual, ax=axes[1,1])
axes[1,1].set_title("Residual KDE")

# Homoscedasticity
axes[1,2].scatter(y_pred, residual)
axes[1,2].set_title("Homoscedasticity")

axes[2,0].plot(residual)
axes[2,0].set_title("Autocorrelation")

# QQ Plot 
import scipy as sp 
sp.stats.probplot(residual, plot=axes[2,1], fit=True) 

axes[2,2].plot(vif)
axes[2,2].set_title("VIF")

plt.tight_layout()
plt.savefig("all_diagnostics.png")
print("Saved: all_diagnostics.png")