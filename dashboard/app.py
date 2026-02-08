import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ==============================
# Page config
# ==============================
st.set_page_config(
    page_title="Climate Trend Analyzer",
    layout="wide"
)

st.title("🌍 Climate Trend Analyzer")
st.write(
    "Interactive dashboard to explore country-wise climate trends "
    "using temperature, rainfall, CO₂ emissions, and sea level data."
)

# ==============================
# Load data
# ==============================
@st.cache_data
def load_data():
    return pd.read_csv("data/processed/climate_master_dataset.csv")

df = load_data()

# ==============================
# Sidebar filters
# ==============================
st.sidebar.header("🔧 Filters")

countries = sorted(df['Country'].unique())
selected_countries = st.sidebar.multiselect(
    "Select Countries",
    countries,
    default=["India", "United States"] if "India" in countries else countries[:2]
)

year_min, year_max = int(df['Year'].min()), int(df['Year'].max())
year_range = st.sidebar.slider(
    "Select Year Range",
    year_min,
    year_max,
    (year_min, year_max)
)

# Apply filters
filtered_df = df[
    (df['Country'].isin(selected_countries)) &
    (df['Year'] >= year_range[0]) &
    (df['Year'] <= year_range[1])
]

# ==============================
# KPI Section
# ==============================
st.subheader("📊 Key Indicators")

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "Avg Temperature",
    f"{filtered_df['Avg_Temperature'].mean():.2f} °C"
)

col2.metric(
    "Avg Rainfall",
    f"{filtered_df['Rainfall_mm'].mean():.1f} mm"
)

col3.metric(
    "Avg CO₂(GtCO2/year)",
    f"{filtered_df['CO2'].mean():.1f}"
)

col4.metric(
    "Avg Sea Level",
    f"{filtered_df['Sea_Level'].mean():.2f} mm"
)

# ==============================
# Plot Helper Function
# ==============================
def create_figure():
    # Reduced figsize slightly to 4x3 for column layout
    fig, ax = plt.subplots(figsize=(4, 3)) 
    return fig, ax

def convert_df_to_csv(df):
    return df.to_csv(index=False).encode('utf-8')

# ==============================
# ROW 1: Temperature & CO2 (Side-by-Side)
# ==============================
st.divider() # Adds a nice visual separator
row1_col1, row1_col2 = st.columns(2)

with row1_col1:
    st.subheader("🌡️ Temperature Trend")
    fig, ax = create_figure()
    for c in selected_countries:
        cdf = filtered_df[filtered_df['Country'] == c]
        ax.plot(cdf['Year'], cdf['Avg_Temperature'], label=c)
    ax.set_xlabel("Year")
    ax.set_ylabel("Avg Temp (°C)")
    ax.legend()
    # use_container_width=True makes it fit the COLUMN, not the whole page
    st.pyplot(fig, use_container_width=True)

with row1_col2:
    st.subheader("🟢 Year-wise CO₂ Trend (GtCO2/year)")
    co2_yearly = filtered_df.groupby('Year')['CO2'].mean().reset_index()
    fig, ax = create_figure()
    ax.plot(co2_yearly['Year'], co2_yearly['CO2'], color='green')
    ax.set_xlabel("Year")
    ax.set_ylabel("CO₂")
    st.pyplot(fig, use_container_width=True)

# ==============================
# ROW 2: Rainfall & Scatter Plot (Side-by-Side)
# ==============================
st.divider()
row2_col1, row2_col2 = st.columns(2)

with row2_col1:
    st.subheader("🌧️ Rainfall Trend")
    rainfall_yearly = filtered_df.groupby('Year')['Rainfall_mm'].mean().reset_index()
    fig, ax = create_figure()
    ax.plot(rainfall_yearly['Year'], rainfall_yearly['Rainfall_mm'], color='blue')
    ax.set_xlabel("Year")
    ax.set_ylabel("Rainfall (mm)")
    st.pyplot(fig, use_container_width=True)

with row2_col2:
    st.subheader("🌧️ vs 🌡️ Relationship")
    fig, ax = create_figure()
    ax.scatter(
        filtered_df['Rainfall_mm'],
        filtered_df['Avg_Temperature'],
        alpha=0.6,
        color='orange'
    )
    ax.set_xlabel("Rainfall (mm)")
    ax.set_ylabel("Avg Temp (°C)")
    st.pyplot(fig, use_container_width=True)

# ==============================
# ROW 3: Sea Level (Centered & Smaller)
# ==============================
st.divider()
st.subheader("🌊 Sea Level Trend")

# Create 3 columns: [Empty, Graph, Empty] to center the graph
left, middle, right = st.columns([1, 2, 1]) 

with middle:
    fig, ax = create_figure()
    for c in selected_countries:
        cdf = filtered_df[filtered_df['Country'] == c]
        ax.plot(cdf['Year'], cdf['Sea_Level'], label=c)
    ax.set_xlabel("Year")
    ax.set_ylabel("Sea Level (mm)")
    ax.legend()
    st.pyplot(fig, use_container_width=True)

# ==============================
# Raw data preview
# ==============================
st.divider()
st.subheader("📄 Data Preview")
view_mode = st.sidebar.radio(
    "Select View Mode",
    ["Summary (Mean values)", "Detailed (Year-wise)"]
)

if view_mode == "Summary (Mean values)":
    summary_df = (
        filtered_df
        .groupby('Country')
        .agg({
            'Avg_Temperature': 'mean',
            'Rainfall_mm': 'mean',
            'CO2': 'mean',
            'Sea_Level': 'mean'
        })
        .reset_index()
        .round(2)
    )
    # Rename column for display only
    summary_df = summary_df.rename(columns={
      'CO2': 'CO2 (GtCO2/year)'
    })
    st.write("Mean values across selected years for each country")
    st.dataframe(summary_df, hide_index=True, use_container_width=True)
    
    st.download_button(
        label="⬇️ Download Summary CSV",
        data=convert_df_to_csv(summary_df),
        file_name="climate_summary_mean.csv",
        mime="text/csv"
    )

else:
    st.write("Year-wise detailed data")
    row_limit = st.slider("Rows to display", 10, 500, 100, 10)
    detailed_df = filtered_df.sort_values(['Country', 'Year']).head(row_limit)
    st.dataframe(detailed_df, hide_index=True, use_container_width=True)

    st.download_button(
        label="⬇️ Download Detailed CSV",
        data=convert_df_to_csv(detailed_df),
        file_name="climate_detailed_yearly.csv",
        mime="text/csv"
    )