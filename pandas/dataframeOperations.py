import pandas as pd
import numpy as np

# Create a more realistic dataset
sales_data = pd.DataFrame({
    'Date': pd.date_range('2024-01-01', periods=100, freq='D'),
    'Product': np.random.choice(['Laptop', 'Mouse', 'Keyboard', 'Monitor'], 100),
    'Sales': np.random.randint(100, 1000, 100),
    'Quantity': np.random.randint(1, 20, 100),
    'Region': np.random.choice(['North', 'South', 'East', 'West'], 100),
    'Customer_Satisfaction': np.random.uniform(1, 5, 100).round(2)
})

# Add some null values
sales_data.loc[10:15, 'Customer_Satisfaction'] = None

print("=" * 50)
print("SALES DATA ANALYSIS")
print("=" * 50)

# 1. Quick peek at the data
print("\n1. FIRST 5 ROWS:")
print(sales_data.head())

print("\n2. LAST 3 ROWS:")
print(sales_data.tail(3))

# 2. Data summary
print("\n3. DATAFRAME INFO:")
print(sales_data.info())

# 3. Statistical summary
print("\n4. STATISTICAL SUMMARY:")
print(sales_data.describe())

# 4. Data dimensions
print("\n5. DATAFRAME DIMENSIONS:")
print(f"Shape: {sales_data.shape}")
print(f"Total records: {len(sales_data)}")
print(f"Total features: {len(sales_data.columns)}")

# 5. Column analysis
print("\n6. COLUMN ANALYSIS:")
print(f"Column names: {sales_data.columns.tolist()}")
print(f"\nData types:\n{sales_data.dtypes}")
print(f"\nMissing values:\n{sales_data.isnull().sum()}")

# 6. Value counts for categorical columns
print("\n7. PRODUCT DISTRIBUTION:")
print(sales_data['Product'].value_counts())

print("\n8. REGION DISTRIBUTION:")
print(sales_data['Region'].value_counts())

# -------------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Emma', 'Frank'],
#     'Age': [25, 30, 35, 28, None, 45],
#     'Salary': [50000, 60000, 75000, 55000, 68000, 90000],
#     'Experience': [2, 5, 8, 3, None, 15]
# })

# print(df[df['Age'] > 30])
# print(df.sort_values('Age'))
# print(df.sort_values(['Age', 'Salary'], ascending=[False, True]))

# filledDf = df.fillna(0)
# print(filledDf)

# dropDf = df.dropna()
# dropDf = df.dropna(how='all')
# dropDf = df.dropna(axis=1)
# print(dropDf)


# --------------------------------------------------------------------------------------------------------------------------

# Sample data: sales by region
# sales = pd.DataFrame({
#     'Region': ['North', 'North', 'South', 'South', 'East', 'West'],
#     'Product': ['A', 'B', 'A', 'B', 'A', 'C'],
#     'Sales': [100, 150, 200, 250, 300, 350],
#     'Quantity': [10, 15, 20, 25, 30, 35]
# })

# Group by single column
# grouped = sales.groupby('Region')
# for name, group in grouped:
#     print(f"Region: {name}")
#     print(group)

# print(sales.groupby('Region').agg({
#     'Sales': ['sum', 'mean'],
#     'Quantity': 'sum'
# }))

# result = sales.groupby('Region').agg(
#     total_sales=('Sales', 'sum'),
#     avg_sales=('Sales', 'mean'),
#     total_qty=('Quantity', 'sum')
# )
# print(result)

# grouped = sales.groupby(['Region', 'Product'])
# print(grouped['Sales'].sum())

# ------------------------------------------------------------------------------------------------------------------------

# # Two DataFrames to merge
# customers = pd.DataFrame({
#     'CustomerID': [1, 2, 3],
#     'Name': ['Alice', 'Bob', 'Charlie']
# })
#
# orders = pd.DataFrame({
#     'OrderID': [101, 102, 103],
#     'CustomerID': [1, 2, 2],
#     'Amount': [250, 300, 150]
# })

# Inner join (default)
# merged = pd.merge(customers, orders, on='CustomerID')
# print(merged)

# Left join
# merged_left = pd.merge(customers, orders, on='CustomerID', how='left')
# print(merged_left)

# Outer join
# merged_outer = pd.merge(customers, orders, on='CustomerID', how='outer')
# print(merged_outer)

# ------------------------------------------------------------------------------------------------------------------------


# data = {
#     "Date": ["01-2024", "02-2024", "01-2024", "02-2024"],
#     "Product": ["A", "A", "B", "B"],
#     "Sales": [100, 150, 200, 250]
# }
#
# df = pd.DataFrame(data)
#
# df = df.pivot(index="Date", columns="Product", values="Sales")
# print(df)

# data = {
#     "Date": ["2024-01", "2024-01", "2024-01"],
#     "Product": ["A", "A", "B"],
#     "Sales": [100, 150, 200]
# }
#
# df = pd.DataFrame(data)
# print(df)
# df = df.pivot_table(
#     index="Date",
#     columns="Product",
#     values="Sales",
#     aggfunc="sum"
# )
# print(df)

# ------------------------------------------------------------------------------------------------------------------------

