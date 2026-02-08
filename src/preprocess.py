import pandas as pd

# 1. Load your dataset
# Replace 'your_original_file.csv' with the actual name of your file
df = pd.read_csv('data/raw/climate_master_dataset_raw.csv')

# 2. Rename the columns to your desired format
df.columns = df.columns.str.strip()
df = df.rename(columns={
    'Country Name': 'Country',
    'Average Temperature': 'Avg_Temperature',
    'Rainfall mm': 'Rainfall_mm',
    'Sea_Level Rise(mm)': 'Sea_Level',
    'CO2 Trend': 'CO2'
})

# 3. Remove duplicate rows
# This removes any row where all values are identical to a previous row
df_clean = df.drop_duplicates()

# 4. Save the result to a new CSV file
# index=False prevents pandas from adding an extra numbering column (0, 1, 2...)
df_clean.to_csv('data/processed/climate_master_dataset.csv', index=False)

print("Success! The cleaned file 'climate_master_dataset.csv' has been created.")
print(df_clean.head())