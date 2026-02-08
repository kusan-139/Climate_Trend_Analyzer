import pandas as pd
import matplotlib.pyplot as plt
import os  

# ==============================
# Setup: Create 'plots' folder
# ==============================
output_folder = "plots"
if not os.path.exists(output_folder):
    os.makedirs(output_folder)
    print(f"✔ Created folder: {output_folder}")

# ==============================
# Load master dataset
# ==============================
df = pd.read_csv("data/processed/climate_master_dataset.csv")

# ==============================
# Basic checks
# ==============================
print(df.head())
print(df.info())

# ==============================
# 1️⃣ GLOBAL TREND: Average Temperature
# ==============================
global_temp = (
    df.groupby('Year')['Avg_Temperature']
      .mean()
      .reset_index()
)

plt.figure(figsize=(10, 6)) # Added size for better readability
plt.plot(global_temp['Year'], global_temp['Avg_Temperature'], color='red')
plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.title("Global Average Temperature Trend")
plt.grid(True)
# SAVE instead of show
plt.savefig(f"{output_folder}/global_temp_trend.png")
plt.close() # Close memory to avoid overlapping plots
print("✔ Saved: global_temp_trend.png")

# ==============================
# 2️⃣ GLOBAL TREND: CO2
# ==============================
# FILTER: Keep only years >= 1990 for CO2 analysis
co2_df = df[df['Year'] >= 1990]

global_co2 = (
    co2_df.groupby('Year')['CO2']
      .mean()
      .reset_index()
)

plt.figure(figsize=(10, 6))
plt.plot(global_co2['Year'], global_co2['CO2'], color='green')
plt.xlabel("Year")
plt.ylabel("CO2 Emissions (per capita)")
plt.title("Global CO2 Trend (1990 - Present)")
plt.grid(True)
plt.savefig(f"{output_folder}/global_co2_trend.png")
plt.close()
print("✔ Saved: global_co2_trend.png")

# ==============================
# 3️⃣ GLOBAL TREND: Sea Level
# ==============================
# Check if Sea Level column exists before plotting
# (Assuming column name is 'Sea Level Rise (mm)' based on previous steps)
sea_col = 'Sea Level Rise (mm)' if 'Sea Level Rise (mm)' in df.columns else 'Sea_Level'

if sea_col in df.columns:
    global_sea = (
        df.groupby('Year')[sea_col]
          .mean()
          .reset_index()
    )

    plt.figure(figsize=(10, 6))
    plt.plot(global_sea['Year'], global_sea[sea_col], color='blue')
    plt.xlabel("Year")
    plt.ylabel("Sea Level Rise (mm)")
    plt.title("Global Sea Level Rise Trend")
    plt.grid(True)
    plt.savefig(f"{output_folder}/global_sea_level_trend.png")
    plt.close()
    print("✔ Saved: global_sea_level_trend.png")

# ==============================
# 4️⃣ COUNTRY COMPARISON (Temperature)
# ==============================
countries = ['India', 'United States', 'China']

plt.figure(figsize=(10, 6))
for c in countries:
    country_df = df[df['Country'] == c]
    plt.plot(country_df['Year'], country_df['Avg_Temperature'], label=c)

plt.xlabel("Year")
plt.ylabel("Average Temperature (°C)")
plt.title("Temperature Trend by Country")
plt.legend()
plt.grid(True)
plt.savefig(f"{output_folder}/country_comparison_temp.png")
plt.close()
print("✔ Saved: country_comparison_temp.png")

# ==============================
# 5️⃣ RELATIONSHIP: Rainfall vs Temperature
# ==============================
plt.figure(figsize=(10, 6))
plt.scatter(df['Rainfall_mm'], df['Avg_Temperature'], alpha=0.5, color='orange')
plt.xlabel("Rainfall (mm)")
plt.ylabel("Average Temperature")
plt.title("Rainfall vs Temperature Relationship")
plt.grid(True)
plt.savefig(f"{output_folder}/scatter_rainfall_vs_temp.png")
plt.close()
print("✔ Saved: scatter_rainfall_vs_temp.png")

print(f"\nAll plots saved successfully in the '{output_folder}' folder.")