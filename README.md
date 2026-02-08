```markdown
# 🌍 Climate Trend Analyzer

A complete **data science project** that analyzes **country-wise climate trends** using a single consolidated dataset.  
The project focuses on **exploratory data analysis (EDA)**, **data preprocessing**, **trend analysis**, and an **interactive Streamlit dashboard**.

---

## 📌 Project Objective

- Analyze long-term climate trends across countries
- Study variations in:
  - Average temperature
  - Rainfall
  - CO₂ emissions
  - Sea level rise
- Provide both **summary-level** and **year-wise detailed insights**
- Build an interactive dashboard for non-technical users

---

## 🗂️ Dataset Used

### ✅ Single Dataset Only

```

climate_data_master_raw.csv

```

This dataset contains **country-wise yearly climate data** with the following fields:

```

Country | Year | Avg_Temperature | Rainfall_mm | CO2 | Sea_Level

```

No other external datasets are used.

---

## ⚙️ Data Preprocessing

The preprocessing step transforms the raw dataset into a clean, analysis-ready dataset.

### Steps performed:
- Standardized column names
- Ensured correct data types (`Country`, `Year`)
- Sorted data by country and year
- Handled missing values using:
  - Country-wise linear interpolation
  - Forward and backward filling for boundary years
- Removed duplicates (if any)

### Output file:
```

climate_data_master.csv

```

Preprocessing logic is implemented in:
```

src/preprocess.py

```

---

## 📊 Exploratory Data Analysis (EDA)

EDA is performed using the processed dataset:

```

climate_data_master.csv

```

### Analysis includes:
- Global trends:
  - Average temperature over time
  - CO₂ emissions trend
  - Rainfall trend
  - Sea level rise trend
- Country-wise comparison of climate indicators
- Long-term variability analysis

EDA code:
```

src/eda.py

```

---

## 📈 Feature Engineering

Light feature engineering is applied to support trend analysis:
- Year-wise grouping
- Country-wise aggregation
- Mean calculations for summary views

No external features or datasets are introduced.

---

## 🤖 Modeling

A **Linear Regression model** is used to understand how climate variables relate to temperature.

### Target variable:
```

Avg_Temperature

```

### Input features:
```

CO2, Rainfall_mm, Sea_Level

```

### Why Linear Regression?
- Simple and interpretable
- Suitable for trend-based climate analysis
- Avoids data leakage
- Easy to explain in viva/interviews

Modeling code:
```

src/model.py

```

---

## 🖥️ Interactive Dashboard (Streamlit)

An interactive dashboard is built using **Streamlit** to explore climate trends visually.

### Dashboard features:
- Country selector (single or multiple)
- Year range slider
- View mode toggle:
  - **Summary view** (mean values per country)
  - **Detailed view** (year-wise data)
- Year-wise trend plots for:
  - Temperature
  - CO₂ emissions
  - Rainfall
  - Sea level rise
- Download buttons:
  - Summary CSV
  - Detailed CSV

Dashboard code:
```

dashboard/app.py

````

### Run the dashboard:
```bash
streamlit run dashboard/app.py
````

---

## 📁 Project Structure

```
Climate_Trend_Analyzer/
│
├── data/
│   ├── raw / climate_data_master_raw.csv
│   └── processed / climate_data_master.csv
│
├── src/
│   ├── preprocess.py
│   ├── eda.py
│   └── model.py
│
├── dashboard/
│   └── app.py
│
└── README.md
```

---

## ▶️ How to Run the Project

```bash
pip install pandas matplotlib scikit-learn streamlit
python src/preprocess.py
python src/eda.py
python src/model.py
streamlit run dashboard/app.py
```


## 📈 Key Insights

* Average temperature shows a long-term increasing trend
* CO₂ emissions rise consistently over the years
* Rainfall patterns vary significantly across countries
* Sea level rise aligns with long-term warming trends
* Climate indicators show strong temporal relationships


## 🚀 Future Improvements

* Time-series forecasting (ARIMA / LSTM)
* Country clustering based on climate patterns
* Normalization of indicators for comparison
* Cloud deployment (Streamlit Cloud)
* Automated report generation


## 🧠 Skills Demonstrated

* Data cleaning and preprocessing
* Exploratory data analysis
* Statistical trend analysis
* Regression modeling
* Interactive dashboard development
* End-to-end project structuring

---

## 👤 Author

**Kusan Chakraborty**  

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to:
- Use
- Modify
- Distribute

This software, provided proper credit is given to the author.

© 2026 Kusan Chakraborty

## 📌 Conclusion

This project demonstrates a **clean, end-to-end climate data analysis pipeline** using a **single consolidated dataset**, emphasizing clarity, interpretability, and usability through interactive visualization.

