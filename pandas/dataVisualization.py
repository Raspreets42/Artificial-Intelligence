import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "Age": [26, 24, 26, 25, 24, 28],
    "Salary": [10, 8, 13, 6, 6, 15]
}

df = pd.DataFrame(data)
# ax = df.plot()

# df["Salary"].plot.hist()

# # Create histograms for all numeric columns in one figure
# df.hist(figsize=(10, 4), bins=10)

# --------------------------------------------------------------------------------------------------------------------

# # Single column with customization
# df['Salary'].plot.hist(
#     bins=10,              # number of bins
#     alpha=0.4,           # transparency
#     color='skyblue',     # bar color
#     edgecolor='black',   # outline color
#     title='Salary Distribution',
#     xlabel='Salary ($)',
#     ylabel='Frequency'
# )

# --------------------------------------------------------------------------------------------------------------------

# # Overlaying Multiple Histograms
# # Two separate Series
# ages_men = [28, 32, 35, 38, 42, 45, 48]
# ages_women = [26, 30, 33, 36, 40, 44, 47]
#
# df_gender = pd.DataFrame({'Men': ages_men, 'Women': ages_women})
#
# df_gender.plot.hist(bins=10, alpha=0.5, figsize=(8, 5))
# plt.title('Age Distribution by Gender')
# plt.xlabel('Age')
# plt.ylabel('Frequency')

# --------------------------------------------------------------------------------------------------------------------

# df['Age'].plot.hist(bins=10, density=True, alpha=0.7)
# plt.title('Age Distribution (Probability Density)')
# plt.ylabel('Density')

# --------------------------------------------------------------------------------------------------------------------

# np.random.seed(42)
# df = pd.DataFrame({'Salary': np.random.gamma(2, 15, 200)})
#
# fig, axes = plt.subplots(1, 3, figsize=(12, 4))
# df['Salary'].plot.hist(bins=5, ax=axes[0], title='5 bins')
# df['Salary'].plot.hist(bins=15, ax=axes[1], title='15 bins')
# df['Salary'].plot.hist(bins='auto', ax=axes[2], title='Auto bins')
# plt.tight_layout()
#
# plt.show()

# --------------------------------------------------------------------------------------------------------------------
#################################   Boxplot     #################################
# --------------------------------------------------------------------------------------------------------------------

# # Sample data
# df = pd.DataFrame({
#     'Age': [25, 30, 35, 40, 45, 50, 55, 60],
#     'Salary': [30, 35, 40, 45, 50, 55, 60, 65]
# })
#
# # Boxplot for all numeric columns
# df.boxplot()
# plt.title('Boxplots of Age and Salary')
# plt.ylabel('Values')
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# # Create data with a group column
# data = {
#     'Department': ['IT', 'IT', 'HR', 'HR', 'IT', 'HR', 'IT', 'HR'],
#     'Salary': [65000, 70000, 55000, 58000, 72000, 60000, 68000, 62000]
# }
# df = pd.DataFrame(data)
#
# # Boxplot of Salary grouped by Department
# df.plot.box(column='Salary', by='Department')
# plt.title('Salary Distribution by Department')
# plt.suptitle('')  # remove default subtitle
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# # Customizing Boxplots
# df = pd.DataFrame({
#     'A': np.random.normal(0, 1, 100),
#     'B': np.random.normal(2, 1.5, 100),
#     'C': np.random.normal(-1, 0.5, 100)
# })
#
# # Customized boxplot
# df.plot.box(
#     figsize=(8, 6),
#     color=dict(boxes='darkblue', whiskers='gray', medians='red', caps='black'),
#     patch_artist=True,          # fill boxes with color
#     notch=True,                 # notch around median
#     vert=True,                  # vertical orientation (default)
#     showmeans=True,             # show mean as a marker
#     meanline=True,              # draw line for mean (instead of marker)
# )
# plt.title('Customized Boxplot')
# plt.show()
#
# # Get outliers for column 'A'
# Q1 = df['A'].quantile(0.25)
# Q3 = df['A'].quantile(0.75)
# IQR = Q3 - Q1
# outliers = df[(df['A'] < Q1 - 1.5*IQR) | (df['A'] > Q3 + 1.5*IQR)]
# print(outliers)

# --------------------------------------------------------------------------------------------------------------------
#################################   Scatterplots     #################################
# --------------------------------------------------------------------------------------------------------------------

# # Sample data
# df = pd.DataFrame({
#     'Age': [25, 26, 28, 30, 44, 37],
#     'Salary': [55000, 80000, 130000, 120000, 110000, 150000]
# })
#
# # df.plot(kind='scatter', x='Age', y='Salary')
# # # df.plot.scatter(x='Age', y='Salary')
# # plt.title('Age vs Salary')
# # plt.show()
#
# # Add a third variable for color (e.g., years of experience)
# df['Experience'] = [1, 3, 5, 7, 10, 12]
#
# df.plot.scatter(
#     x='Age',
#     y='Salary',
#     c='Experience',          # color points by Experience
#     cmap='viridis',          # colormap
#     s=100,                   # marker size
#     alpha=0.7,               # transparency
#     edgecolors='black',      # outline color
#     title='Age vs Salary (colored by Experience)'
# )
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# # Create a DataFrame with four variables
# df2 = pd.DataFrame({
#     'Height': [150, 160, 170, 180, 190],
#     'Weight': [55, 65, 75, 85, 95],
#     'Age': [20, 30, 40, 50, 60],
#     'Salary': [30000, 90000, 170000, 230000, 260000]
# })

# # Scatterplot with size = Age, color = Salary
# df2.plot.scatter(
#     x='Height',
#     y='Weight',
#     s='Age',                 # size based on Age
#     c='Salary',              # color based on Salary
#     cmap='plasma',
#     alpha=0.8,
#     title='Height vs Weight (size=Age, color=Salary)'
# )
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# Sample data
df = pd.DataFrame({
    'Age': [25, 26, 28, 30, 44, 37],
    'Salary': [55000, 80000, 130000, 120000, 110000, 150000]
})
# Add a third variable for color (e.g., years of experience)
df['Experience'] = [1, 3, 5, 7, 10, 12]

# fig, axes = plt.subplots(2, 1, figsize=(12, 4))
#
# # Left plot: Age vs Salary
# df.plot.scatter(x='Age', y='Salary', ax=axes[0], color='blue', alpha=0.6)
# axes[0].set_title('Age vs Salary')
#
# # Right plot: Experience vs Salary
# df.plot.scatter(x='Experience', y='Salary', ax=axes[1], color='red', alpha=0.6)
# axes[1].set_title('Experience vs Salary')
#
# plt.tight_layout()
# plt.show()

# from pandas.plotting import scatter_matrix
#
# df_num = df[['Age', 'Salary', 'Experience']]
# scatter_matrix(df_num, alpha=0.5, figsize=(8, 8), diagonal='hist')
# plt.show()

# --------------------------------------------------------------------------------------------------------------------
#################################   Pie Charts     #################################
# --------------------------------------------------------------------------------------------------------------------

# # Sample data: sales by product category
# sales = pd.Series([350, 450, 200], index=['Laptops', 'Tablets', 'Phones'])
#
# sales.plot.pie()
# plt.title('Sales Distribution')
# plt.ylabel('')   # remove default 'y' label
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Category': ['A', 'B', 'C', 'D'],
#     'Value': [25, 35, 20, 20]
# })
#
# df.set_index('Category')['Value'].plot.pie()
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# # Sample data
# sales = pd.Series([350, 450, 200], index=['Laptops', 'Tablets', 'Phones'])
#
# sales.plot.pie(
#     autopct='%1.1f%%',      # show percentages
#     explode=[0, 0, 0.3], # pull out slices
#     shadow=True,            # add shadow
#     startangle=0,          # rotate start angle
#     colors=['skyblue', 'lightgreen', 'lightcoral'],
#     wedgeprops={'edgecolor': 'black', 'linewidth': 1}
# )
# plt.title('Customized Pie Chart')
# plt.ylabel('')
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Product A': [30, 50, 20],
#     'Product B': [40, 40, 20],
#     'Product C': [25, 35, 40]
# }, index=['Region 1', 'Region 2', 'Region 3'])
#
# # One pie per column (subplots)
# df.plot.pie(subplots=True, figsize=(12, 4), autopct='%1.1f%%')
# plt.tight_layout()
# plt.show()

# --------------------------------------------------------------------------------------------------------------------
#################################   SLine Plot     #################################
# --------------------------------------------------------------------------------------------------------------------

# # Sample data: monthly sales
# sales = pd.Series([200, 220, 250, 280, 310, 330],
#                   index=['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
#
# sales.plot()
# plt.title('Monthly Sales')
# plt.ylabel('Sales ($)')
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

# df = pd.DataFrame({
#     'Year': [2015, 2016, 2017, 2018, 2019, 2020],
#     'Sales': [500, 550, 600, 620, 700, 750],
#     'Expenses': [400, 420, 450, 480, 520, 600]
# })
#
# # Set Year as index and plot
# df.set_index('Year').plot()
# plt.title('Sales vs Expenses Over Years')
# plt.ylabel('Amount ($)')
# plt.show()

# # Customized line plot
# df.set_index('Year').plot(
#     style=['r--o', 'b-^'],      # line style: red dashed with circle markers, blue solid with triangle markers
#     linewidth=2,                # line thickness
#     alpha=0.7,                  # transparency
#     grid=True,                  # show grid
#     title='Financial Trends',
#     xlabel='Year',
#     ylabel='Amount ($)',
#     legend=True,
#     figsize=(8, 5)
# )
# plt.show()

# Multiple Lines on the Same Plot (Manually)
# plt.plot(df['Year'], df['Sales'], 'g-', label='Sales', linewidth=2)
# plt.plot(df['Year'], df['Expenses'], 'r--', label='Expenses', linewidth=2)
# plt.xlabel('Year')
# plt.ylabel('Amount ($)')
# plt.title('Sales vs Expenses')
# plt.legend()
# plt.grid(True)
# plt.show()

# Subplots (One Plot per Column)
# df.set_index('Year').plot(subplots=True, layout=(2,1), figsize=(8, 6))
# plt.tight_layout()
# plt.show()

# --------------------------------------------------------------------------------------------------------------------

date_rng = pd.date_range(start='2024-01-01', periods=30, freq='D')
df_ts = pd.DataFrame({
    'Date': date_rng,
    'Value': [i + (i%7) for i in range(30)]   # some pattern
})
df_ts.set_index('Date').plot()
plt.title('Daily Time Series')
plt.show()
