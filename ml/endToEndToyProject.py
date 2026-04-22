import numpy as np
import pandas as pd

# step 1 : Data collection
df = pd.read_csv('placement.csv')

# step 2 : Data preprocess
df = df.iloc[:, 1:] # drops the first column:
# : (before the comma) → select all rows.
# 1: (after the comma) → select columns starting from index 1

# step 3 : EDA
import matplotlib.pyplot as plt
plt.scatter(df['cgpa'], df['iq'], c=df['placement'])
plt.show()

# step 4 : Extract input and output columns
input = df.iloc[:, 0:2] # column 0th and 1st
output = df.iloc[:, -1] # column last

# step 5 : Train test split
from sklearn.model_selection import train_test_split
input_train, input_test, output_train, output_test = train_test_split(input, output, test_size=0.1) # test_size=0.1 will have 10% i.e. 10 rows out of 100 rows
# print("input_train :: ", input_train)
# print("input_test :: ", input_test)
# print("output_train :: ", output_train)
# print("output_test :: ", output_test)

# Optional
# fig, (ax1, ax2) =plt.subplots(ncols=2, figsize=(15, 5))
# ax1.scatter(input_train['cgpa'], input_train['iq'], color='black')

# step 6 : Scale the values
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
input_train = scaler.fit_transform(input_train)
# print("input_train :: ", input_train)
input_test = scaler.fit_transform(input_test)
# print("input_test :: ", input_test)

# Optional
# input_train_scaled = pd.DataFrame(input_train, columns=['cgpa', 'iq'])
# input_test_scaled = pd.DataFrame(input_test, columns=['cgpa', 'iq'])
# ax2.scatter(input_train_scaled['cgpa'], input_train_scaled['iq'], color='red')
# plt.show()

# step 7 : train the model
from sklearn.linear_model import LogisticRegression
clsifier = LogisticRegression()
clsifier.fit(input_train, output_train)     # model training

# step 8 : Evaluate the model
output_pred = clsifier.predict(input_test)
# print("output_pred :: ", output_pred)
# print("output_test :: ", output_test)

# step 9 : accuracy check
from sklearn.metrics import accuracy_score
acc = accuracy_score(output_test, output_pred)
print("acc :: ", acc)

# step 10 : Decision Boundary Visualization
from mlxtend.plotting import plot_decision_regions
plot_decision_regions(input_train, output_train.values, clf=clsifier, legend=2)
plt.show()

#step 11 : showcase in website
import pickle
pickle.dump(clsifier, open('model.pkl', 'wb'))