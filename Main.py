import pandas as pd
import matplotlib.pyplot as plt
import os

print("=== Improved Visualization for Beans Production ===\n")

df = pd.read_csv('data/cleaned_beans_data.csv')

# Filter Beans
if 'Item' in df.columns:
    df = df[df['Item'].str.contains('Bean', case=False, na=False)].copy()

print(f"Total Beans rows: {len(df)}")
print("Years available:", sorted(df['Year'].unique()) if 'Year' in df.columns else "No Year")

os.makedirs('outputs', exist_ok=True)

# Plot 1: Trend (bigger, clearer)
plt.figure(figsize=(12, 7))
yearly = df.groupby('Year')['Value'].mean()
yearly.plot(kind='line', marker='o', color='darkgreen', linewidth=3, markersize=8)
plt.title('Beans Production Trend (2015-2024)', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Average Production Value', fontsize=12)
plt.grid(True)
plt.xticks(yearly.index)   # Show all years
plt.savefig('outputs/01_trend_analysis.png')
plt.show()

# Plot 2: Bar Chart
plt.figure(figsize=(12, 7))
if 'Element' in df.columns and df['Element'].nunique() > 1:
    df.groupby('Element')['Value'].mean().plot(kind='bar', color='orange')
    plt.title('Beans Production by Element', fontsize=14)
else:
    df.groupby('Area')['Value'].mean().plot(kind='bar', color='orange')
    plt.title('Beans Production by Area', fontsize=14)
plt.ylabel('Average Value', fontsize=12)
plt.grid(True)
plt.savefig('outputs/02_categorical_comparison.png')
plt.show()

# Plot 3: Scatter with better scale
plt.figure(figsize=(12, 7))
plt.scatter(df['Year'], df['Value'], alpha=0.8, color='blue', s=100)
plt.title('Year vs Beans Production Value', fontsize=14)
plt.xlabel('Year', fontsize=12)
plt.ylabel('Production Value', fontsize=12)
plt.grid(True)
plt.savefig('outputs/03_correlation_plot.png')
plt.show()

print("\n✅ Improved graphs generated!")