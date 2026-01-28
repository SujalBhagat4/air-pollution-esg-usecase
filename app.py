import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="ESG Air Pollution Dashboard", layout="centered")

# Title
st.title("Air Pollution Visualization Dashboard")

st.markdown("### Select Parameters")

# Pollutant selection
pollutant = st.selectbox(
    "Select Pollutant",
    ["NO₂"]
)

# Time selection
time_range = st.selectbox(
    "Select Time Range",
    ["Last 24 hours", "Last 7 days", "Last 30 days"]
)

# Region selection
region = st.selectbox(
    "Select Region",
    ["Delhi", "Mumbai", "Bangalore"]
)

# Button
if st.button("Generate Visualization"):

    st.success(f"Showing {pollutant} levels for {region} ({time_range})")

    # Dummy data for visualization
    x = np.arange(10)
    y = np.random.randint(20, 100, size=10)

    # Plot
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_xlabel("Time")
    ax.set_ylabel("NO₂ Concentration")
    ax.set_title("NO₂ Pollution Levels")

    st.pyplot(fig)
    
