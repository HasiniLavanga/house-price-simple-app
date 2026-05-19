import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide"
)

st.title("🏠 House Price Prediction & Valuation Tool")

st.markdown("""
This interactive web application estimates house prices 
based on property characteristics using a prediction system.
""")

st.sidebar.header("Property Features")

overall_quality = st.sidebar.slider("Overall Quality", 1, 10, 5)

living_area = st.sidebar.number_input(
    "Living Area (sq ft)",
    min_value=500,
    max_value=5000,
    value=1500
)

garage_cars = st.sidebar.slider(
    "Garage Capacity",
    0,
    5,
    2
)

year_built = st.sidebar.slider(
    "Year Built",
    1900,
    2025,
    2005
)

basement_area = st.sidebar.number_input(
    "Basement Area",
    min_value=0,
    max_value=3000,
    value=800
)

if st.button("Predict House Price"):

    estimated_price = (
        overall_quality * 50000
        + living_area * 120
        + garage_cars * 15000
        + basement_area * 40
        + (year_built - 2000) * 1000
    )

    st.success(f"🏡 Estimated House Price: ${estimated_price:,.2f}")

    prediction_data = pd.DataFrame({
        "Feature": [
            "Overall Quality",
            "Living Area",
            "Garage Capacity",
            "Basement Area",
            "Year Built"
        ],
        "Value": [
            overall_quality,
            living_area,
            garage_cars,
            basement_area,
            year_built
        ]
    })

    st.subheader("📊 Property Summary")

    st.dataframe(prediction_data, use_container_width=True)

st.markdown("---")

st.caption("Machine Learning House Price Prediction Project using Streamlit")