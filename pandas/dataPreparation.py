import pandas as pd
import numpy as np

# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob', 'Bob'],
#     'Age': [25, 30, 25, 35, 30, 28],
#     'City': ['NYC', 'LA', 'NYC', 'Chicago', 'LA', 'LA']
# })
#
# print("Original DataFrame:")
# print(df)
#
# print("\nAfter drop_duplicates() (all columns):")
# df.drop_duplicates(subset=['Name'], keep=False, inplace=True)
# print(df)

# ----------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Employee Name': ['Ashwin', 'Bharat', 'Dolly', 'Nishant', 'Raspreet', 'Sailesh'],
#     'Age': [28, 28, 27, 26, 26, 25],
#     'City': ['Nagpur', 'Vizag', 'Gurgaon', 'Nagpur', 'Bhilai', 'Nagpur']
# })
# print(df.rename(columns={'Employee Name': "Name"}, inplace=False))
# print(df.rename(index={0: "Row0"}, inplace=False))

# ----------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Employee Name': ['Ashwin', 'Bharat', 'Dolly', 'Nishant', 'Raspreet', 'Sailesh'],
#     'Age': [28, 18, 77, 46, 16, 25],
#     'City': ['Nagpur', 'Vizag', 'Gurgaon', 'Nagpur', 'Bhilai', 'Nagpur']
# })
# df["AgeGroup"] = pd.cut(
#     df["Age"],
#     bins=[0, 18, 35, 60, np.inf],
#     labels=["Child", "Adult", "Senior", "Aged"]
# )
# print(df)
# indicator_df = pd.get_dummies(df, columns=['AgeGroup'])
# print(indicator_df)

# ----------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Employee Name': ['Ashwin', 'Bharat', 'Dolly', 'Nishant', 'Sailesh'],
#     'Salary': [28, 16, 18, 7, 8],
# })
# # df["Rank"] = df["Salary"].rank()
# print(df.describe())

# ----------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Department': ['IT', 'HR', 'IT', 'HR', 'IT', 'Finance'],
#     'Gender': ['Male', 'Female', 'Male', 'Female', 'Female', 'Male']
# })
#
# # # # Count of employees by department and gender
# # # ct = pd.crosstab(df['Department'], df['Gender'])
# # # print(ct)
# #
# # ct = pd.crosstab(df['Department'], df['Gender'], margins=True, margins_name='Total')
# # print(ct)
#
# ct_norm = pd.crosstab(df['Department'], df['Gender'], normalize='index')
# print(ct_norm.round(2))
# ct_norm = pd.crosstab(df['Department'], df['Gender'], normalize='columns')
# print(ct_norm.round(2))

# ----------------------------------------------------------------------------------------------------------------------

# sales = pd.DataFrame({
#     'Region': ['North', 'North', 'South', 'South'],
#     'Product': ['A', 'B', 'A', 'B'],
#     'Sales': [100, 150, 200, 250]
# })
#
# # Average sales by Region and Product
# ct = pd.crosstab(index=sales['Region'],
#                  columns=sales['Product'],
#                  values=sales['Sales'],
#                  aggfunc='mean')
# print(ct)

# ----------------------------------------------------------------------------------------------------------------------
