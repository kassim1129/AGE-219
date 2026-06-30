import pandas as pd
import os

print("=== Beans Production Data Cleaning (2015-2024) ===\n")

DATA_DIR = 'data/'
OUTPUT_FILE = 'data/cleaned_beans_data.csv'

# Step 1: List all CSV files
csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
print(f"Found {len(csv_files)} files: {csv_files}\n")

# Step 2: Read and combine
dfs = []
for file in csv_files:
    filepath = os.path.join(DATA_DIR, file)
    df = pd.read_csv(filepath)
    df['source_file'] = file
    dfs.append(df)
    print(f"Loaded {file} - {len(df)} rows")

# Combine
merged = pd.concat(dfs, ignore_index=True)
print(f"\nTotal rows before cleaning: {len(merged)}")

# Step 3: Filter years 2015-2024
if 'Year' in merged.columns:
    merged['Year'] = pd.to_numeric(merged['Year'], errors='coerce')
    merged = merged[(merged['Year'] >= 2015) & (merged['Year'] <= 2024)]
    print(f"Rows after 2015-2024 filter: {len(merged)}")

# Step 4: Cleaning
# Fill missing numbers with median
numeric_cols = merged.select_dtypes(include=['number']).columns
merged[numeric_cols] = merged[numeric_cols].fillna(merged[numeric_cols].median())

# Drop rows where important columns are missing
important_cols = ['Year']
if 'Production' in merged.columns:
    important_cols.append('Production')
merged.dropna(subset=important_cols, inplace=True)

print("\n=== Final Cleaned Data Info ===")
print(merged.info())
print("\nSample data:")
print(merged.head())

# Save cleaned data
merged.to_csv(OUTPUT_FILE, index=False)
print(f"\n✅ Cleaned data saved as: {OUTPUT_FILE}")