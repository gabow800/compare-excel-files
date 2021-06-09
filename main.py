import pandas as pd
import numpy as np

# Load data
file_a = pd.read_excel('file-a.xlsx')
file_b = pd.read_excel('file-b.xlsx')

# Get rows and columns that differ
comparison = file_a == file_b
rows, cols = np.where(comparison == False)

# Highlight differences in file
for row, col in zip(rows, cols):
    file_a_value = file_a.iloc[row, col]
    file_b_value = file_b.iloc[row, col]
    file_a.iloc[row, col] = f"{file_a_value} -> {file_b_value}"

# Extract rows with differences
result = pd.DataFrame(file_a.iloc[rows])

print(result)
result.to_excel('result.xlsx')
