import pandas as pd
import matplotlib.pyplot as plt
import os

print("=== Beans Production Visualization (2015-2024) ===\n")

# Load the cleaned file
df = pd.read_csv('data/cleaned_beans_data.csv')

# Filter only Beans
if 'Item' in df.columns:
    df = df[df['Item'].str.contains('Bean', case=False, na=False)].copy()
    print(f"Using Beans data: {len(df)} rows")

os.makedirs('outputs', exist_ok=True)

# Plot 1: Trend Analysis
plt.figure(figsize=(10, 6))
yearly = df.groupby('Year')['Value'].mean()
yearly.plot(kind='line', marker='o', color='darkgreen', linewidth=2.5)
plt.title('Beans Production Trend (2015-2024)')
plt.xlabel('Year')
plt.ylabel('Average Production Value')
plt.grid(True)
plt.savefig('outputs/01_trend_analysis.png')
plt.show()

# Plot 2: Categorical Comparison
plt.figure(figsize=(10, 6))
if 'Element' in df.columns and df['Element'].nunique() > 1:
    df.groupby('Element')['Value'].mean().plot(kind='bar', color='orange')
    plt.title('Beans Production by Element')
else:
    df.groupby('Area')['Value'].mean().plot(kind='bar', color='orange')
    plt.title('Beans Production by Area')
plt.ylabel('Average Value')
plt.grid(True)
plt.savefig('outputs/02_categorical_comparison.png')
plt.show()

# Plot 3: Correlation
plt.figure(figsize=(10, 6))
plt.scatter(df['Year'], df['Value'], alpha=0.7, color='blue')
plt.title('Correlation: Year vs Beans Production Value')
plt.xlabel('Year')
plt.ylabel('Production Value')
plt.grid(True)
plt.savefig('outputs/03_correlation_plot.png')
plt.show()

print("\n✅ All 3 plots saved in the 'outputs' folder!")