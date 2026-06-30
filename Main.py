import pandas as pd
import os

print("=== Re-running Cleaning ===\n")

DATA_DIR = 'data/'
OUTPUT_FILE = 'data/cleaned_beans_data.csv'

csv_files = [f for f in os.listdir(DATA_DIR) if f.endswith('.csv')]
print(f"Found {len(csv_files)} files")

dfs = []
for file in csv_files:
    df = pd.read_csv(os.path.join(DATA_DIR, file))
    df['source_file'] = file
    dfs.append(df)

merged = pd.concat(dfs, ignore_index=True)

# Filter years
if 'Year' in merged.columns:
    merged['Year'] = pd.to_numeric(merged['Year'], errors='coerce')
    merged = merged[(merged['Year'] >= 2015) & (merged['Year'] <= 2024)]

# Cleaning
numeric_cols = merged.select_dtypes(include=['number']).columns
merged[numeric_cols] = merged[numeric_cols].fillna(merged[numeric_cols].median())

merged.to_csv(OUTPUT_FILE, index=False)
print(f"✅ Cleaned file saved: {OUTPUT_FILE}")
print("Number of rows:", len(merged))
print("Columns:", merged.columns.tolist())