# ======================================
# Sales Data Analysis using Pandas
# Week 3 Internship Project
# ======================================

# Import pandas library
import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

print("=" * 50)
print("Sales Dataset")
print("=" * 50)

# Display first five rows
print("\nFirst 5 Rows")
print(df.head())

# Dataset information
print("\nDataset Information")
print(df.info())

# Shape
print("\nRows and Columns")
print(df.shape)

# Column names
print("\nColumns")
print(df.columns)

# Missing values
print("\nMissing Values")
print(df.isnull().sum())

# Fill missing quantity with 1
df["Quantity"] = df["Quantity"].fillna(1)

# Remove duplicate rows
df = df.drop_duplicates()

# Create Total Sales column
df["Total_Sales"] = df["Quantity"] * df["Price"]

print("\nUpdated Dataset")
print(df)

# -----------------------------
# Analysis
# -----------------------------

# Total Revenue
total_revenue = df["Total_Sales"].sum()

# Highest Sale
highest_sale = df["Total_Sales"].max()

# Lowest Sale
lowest_sale = df["Total_Sales"].min()

# Average Sale
average_sale = df["Total_Sales"].mean()

# Best Selling Product
best_product = (
    df.groupby("Product")["Quantity"]
      .sum()
      .idxmax()
)

# Product Wise Sales
product_sales = df.groupby("Product")["Total_Sales"].sum()

# -----------------------------
# Report
# -----------------------------

print("\n")
print("=" * 50)
print("SALES ANALYSIS REPORT")
print("=" * 50)

print(f"Total Revenue       : ₹{total_revenue:,.2f}")
print(f"Highest Sale        : ₹{highest_sale:,.2f}")
print(f"Lowest Sale         : ₹{lowest_sale:,.2f}")
print(f"Average Sale        : ₹{average_sale:,.2f}")
print(f"Best Selling Product: {best_product}")

print("\nProduct Wise Revenue")

print(product_sales)

print("\nAnalysis Completed Successfully!")