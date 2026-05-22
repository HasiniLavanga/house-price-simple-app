import pandas as pd
from scipy.stats import pearsonr

# Load dataset
df = pd.read_csv("AmesHousing.csv")

print("Dataset Loaded Successfully")

print("\nFIRST 5 ROWS:")
print(df.head())

print("\nCOLUMN NAMES:")
print(df.columns)

# Hypothesis Testing
corr, p_value = pearsonr(df['Gr Liv Area'], df['SalePrice'])

print("\n===== HYPOTHESIS TESTING RESULTS =====")

print("Correlation:", corr)
print("P-value:", p_value)

if p_value < 0.05:
    print("\nReject Null Hypothesis")
    print("Living area significantly affects house price.")
else:
    print("\nFail to Reject Null Hypothesis")