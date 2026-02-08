import pandas as pd
import numpy as np  # Required for square root calculation
import os           # Required for folder creation
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plt

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
# Select features & target
# ==============================
# Check for Sea Level column name variations
sea_col = 'Sea Level Rise (mm)' if 'Sea Level Rise (mm)' in df.columns else 'Sea_Level'

features = ['CO2', 'Rainfall_mm', sea_col]
target = 'Avg_Temperature'

# Ensure these columns exist
df_model = df[features + [target]].dropna()

X = df_model[features]
y = df_model[target]

# ==============================
# Train-test split
# ==============================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# ==============================
# Train Linear Regression model
# ==============================
model = LinearRegression()
model.fit(X_train, y_train)

# ==============================
# Predictions
# ==============================
y_pred = model.predict(X_test)

# ==============================
# Evaluation (Fixed for modern sklearn)
# ==============================
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)  # Calculate RMSE manually

r2 = r2_score(y_test, y_pred)

print("Model Performance:")
print("RMSE:", rmse)
print("R² Score:", r2)

# ==============================
# Coefficients
# ==============================
coefficients = pd.DataFrame({
    'Feature': features,
    'Coefficient': model.coef_
})

print("\nModel Coefficients:")
print(coefficients)

# ==============================
# Save Actual vs Predicted plot
# ==============================
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
# Add a red diagonal line for perfect prediction reference
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'r--', lw=2)

plt.xlabel("Actual Temperature")
plt.ylabel("Predicted Temperature")
plt.title("Actual vs Predicted Temperature (Model Performance)")
plt.grid(True)

# SAVE the plot
save_path = f"{output_folder}/model_actual_vs_predicted.png"
plt.savefig(save_path)
plt.close()

print(f"✔ Plot saved successfully to: {save_path}")