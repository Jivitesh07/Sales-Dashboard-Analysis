import pandas as pd
import os

# Define the expected file name based on the original task
FILE_NAME = 'Superstore_Sales.csv'

# --- 1. Import the CSV file ---
try:
    # Attempt to read the CSV file
    df = pd.read_csv(r"C:\Users\jivit\OneDrive\Documents\Matplotib & Seaborn\Sales_data.csv")
    print(f"Data imported successfully from {FILE_NAME}!")

except FileNotFoundError:
    print(f"Error: The file '{FILE_NAME}' was not found in the current directory.")
    print("Please ensure the file is present or update the 'FILE_NAME' variable with the correct path.")
    exit()

# Display the initial structure to check data types
print("\n--- Initial DataFrame Info ---")
df.info()

# --- 2. Convert Order Date to “Month-Year” format and ensure Sales is numeric ---

# Convert 'Order Date' to datetime objects
if 'Order Date' in df.columns:
    df['Order Date'] = pd.to_datetime(df['Order Date'])

    # Create a new column 'Month-Year' for time series visualization
    # The format '%Y-%m' is used for correct chronological sorting in dashboard tools
    df['Month-Year'] = df['Order Date'].dt.strftime('%Y-%m')
else:
    print("\n⚠️ Warning: 'Order Date' column not found. Time-series analysis skipped.")

# Ensure 'Sales' column is numeric
if 'Sales' in df.columns:
    # Basic cleaning (uncomment if your sales column contains '$' or ',')
    # df['Sales'] = df['Sales'].astype(str).str.replace('$', '').str.replace(',', '').astype(float)
    df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce') # 'coerce' turns bad values into NaN
else:
    print("\n⚠️ Warning: 'Sales' column not found. Sales aggregation skipped.")


# --- 3. Basic Aggregation (Preparing Data for Visuals) ---

# A. Sales over Months (for Line Chart)
if all(col in df.columns for col in ['Month-Year', 'Sales']):
    sales_over_months = df.groupby('Month-Year')['Sales'].sum().reset_index()
    print("\n--- Sales Over Months Data Preview ---")
    print(sales_over_months.tail())
else:
    print("\n--- Sales Over Months Data Skipped ---")

# B. Sales by Region (for Bar Chart)
if all(col in df.columns for col in ['Region', 'Sales']):
    sales_by_region = df.groupby('Region')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
    print("\n--- Sales by Region Data Preview ---")
    print(sales_by_region)
else:
    print("\n--- Sales by Region Data Skipped ---")

# C. Sales by Category (for Donut Chart)
if all(col in df.columns for col in ['Category', 'Sales']):
    sales_by_category = df.groupby('Category')['Sales'].sum().reset_index().sort_values(by='Sales', ascending=False)
    print("\n--- Sales by Category Data Preview ---")
    print(sales_by_category)
else:
    print("\n--- Sales by Category Data Skipped ---")