import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("AmesHousing.csv")

print(df.head())

# Scatter Plot
plt.figure(figsize=(8,5))

sns.scatterplot(
    x=df['Gr Liv Area'],
    y=df['SalePrice']
)

plt.title("Living Area vs Sale Price")

plt.xlabel("Living Area")

plt.ylabel("Sale Price")

plt.savefig("area_vs_price.png")

plt.show()

# Heatmap
plt.figure(figsize=(12,8))

numeric_df = df.select_dtypes(include=['number'])

sns.heatmap(
    numeric_df.corr(),
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")

plt.savefig("heatmap.png")

plt.show()

print("\nVisualizations created successfully.")