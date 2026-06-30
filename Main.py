import pandas as pd

print("=== Beans Production Data Analysis ===\n")

# Load cleaned data
df = pd.read_csv('data/cleaned_beans_data.csv')

# Filter Beans only
if 'Item' in df.columns:
    df_beans = df[df['Item'].str.contains('Bean', case=False, na=False)].copy()
    print(f"Found Beans data: {len(df_beans)} rows")
else:
    df_beans = df.copy()
    print("Using all data")

print("\nAvailable Columns:", df_beans.columns.tolist())

print("\n=== Summary Statistics ===")
print(df_beans.describe())

print("\n=== Average Value by Year ===")
if 'Year' in df_beans.columns:
    yearly = df_beans.groupby('Year')['Value'].mean()
    print(yearly)

print("\n=== Average Value by Area ===")
if 'Area' in df_beans.columns:
    print(df_beans.groupby('Area')['Value'].mean())

print("\n=== Average Value by Element ===")
if 'Element' in df_beans.columns:
    print(df_beans.groupby('Element')['Value'].mean())

print("\n✅ Analysis completed. Data looks good!")