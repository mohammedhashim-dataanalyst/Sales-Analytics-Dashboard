# Sales Analytics Project
# Author: Mohammed Hashim

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Dataset
df = pd.read_csv("sales.csv")

# Data Cleaning
df.drop_duplicates(inplace=True)
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Create Revenue Column
if 'Revenue' not in df.columns:
    df['Revenue'] = df['Sales'] * df['Quantity']

# Monthly Revenue Trend
monthly_sales = df.groupby(df['Order Date'].dt.to_period('M'))['Revenue'].sum()

plt.figure(figsize=(10,5))
monthly_sales.plot()
plt.title("Monthly Revenue Trend")
plt.xlabel("Month")
plt.ylabel("Revenue")
plt.show()

# Top 10 Products
top_products = df.groupby('Product Name')['Revenue'].sum().sort_values(ascending=False).head(10)
print("\nTop 10 Products by Revenue:\n")
print(top_products)

# Region Wise Revenue
region_sales = df.groupby('Region')['Revenue'].sum()

plt.figure(figsize=(8,4))
region_sales.plot(kind='bar')
plt.title("Region Wise Revenue")
plt.show()

# Export Cleaned Data
df.to_csv("sales_cleaned.csv", index=False)

print("\nAnalysis Completed Successfully.")
