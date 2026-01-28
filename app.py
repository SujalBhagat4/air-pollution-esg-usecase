import streamlit as st
import xarray as xr
import matplotlib.pyplot as plt
import numpy as np

st.title("Air Pollution Visualization Dashboard")

# ---- User Inputs ----
pollutant = st.selectbox("Select Pollutant", ["NO₂"])
region = st.text_input("Enter Region (example: Delhi)")
time_range = st.selectbox("Select Time Range", ["Daily", "Weekly", "Monthly"])

st.write("Selected:")
st.write("Pollutant:", pollutant)
st.write("Region:", region)
st.write("Time Range:", time_range)

# ---- Button ----
if st.button("Generate Visualization"):
    st.subheader("Visualization Output")

    # Dummy data for prototype
    x = np.arange(10)
    y = np.random.rand(10)

    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set_title("NO₂ Concentration Trend")
    ax.set_xlabel("Time")
    ax.set_ylabel("NO₂ Level")

    st.pyplot(fig)
