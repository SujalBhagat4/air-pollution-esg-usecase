import streamlit as st
import pandas as pd
import numpy as np

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="ESG Air Pollution Dashboard",
    page_icon="🌍",
    layout="wide"
)

# ---------------- TITLE ----------------
st.title("🌍 ESG Air Pollution Monitoring Dashboard")

st.markdown("""
This interactive dashboard visualizes **air pollution trends (NO₂)**  
to support **ESG analysis, sustainability monitoring, and environmental insights**.
""")

# ---------------- SIDEBAR PARAMETERS ----------------
st.sidebar.header("⚙️ Select Parameters")

pollutant = st.sidebar.selectbox(
    "Pollutant",
    ["NO₂"]
)

region = st.sidebar.selectbox(
    "Region",
    ["India", "Delhi", "Mumbai", "Bangalore"]
)

time_range = st.sidebar.slider(
    "Time Range (Year)",
    2018, 2024, (2020, 2023)
)

# ---------------- SUMMARY METRICS ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Pollutant Selected", pollutant)

with col2:
    st.metric("Region Selected", region)

with col3:
    st.metric("Time Span", f"{time_range[0]} - {time_range[1]}")

# ---------------- DATA (DUMMY – PROTOTYPE) ----------------
years = list(range(time_range[0], time_range[1] + 1))
pollution_values = np.random.randint(20, 60, size=len(years))

data = pd.DataFrame({
    "Year": years,
    "NO2 Level": pollution_values
})

# ---------------- VISUALIZATION ----------------
st.subheader("📊 NO₂ Pollution Trend")

st.line_chart(
    data.set_index("Year")
)

# ---------------- INSIGHTS ----------------
st.subheader("🧠 Key Observations")

st.write("""
- NO₂ levels show **variation across selected years**
- Urban regions indicate **higher pollution intensity**
- This model can be extended with **real satellite datasets**
""")

# ---------------- FOOTER ----------------
st.success("Dashboard generated successfully based on selected parameters.")
