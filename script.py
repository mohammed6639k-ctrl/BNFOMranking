import pandas as pd
import numpy as np

# Load the Excel file to understand its structure
file_path = "trtyb-tlth-Copy.xlsx"

# First, let's see what sheets are available
xl = pd.ExcelFile(file_path)
print("Available sheets:", xl.sheet_names)

# Load the first sheet to examine the data structure
df = pd.read_excel(file_path, sheet_name=0)
print("\nDataFrame shape:", df.shape)
print("\nColumn names:")
print(df.columns.tolist())
print("\nFirst few rows:")
print(df.head())
print("\nData types:")
print(df.dtypes)