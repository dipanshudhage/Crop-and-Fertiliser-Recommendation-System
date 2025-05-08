import streamlit as st
import pandas as pd
import joblib

# Load trained models and label encoders
crop_model = joblib.load("model_crop.pkl")
crop_le = joblib.load("label_encoder_crop.pkl")
fert_model = joblib.load("model_fertilizer.pkl")
fert_le = joblib.load("label_encoder_fertilizer.pkl")

# Streamlit app title and intro
st.set_page_config(page_title="Crop & Fertilizer Recommendation", page_icon="🌾")
st.title("🌾 Crop and Fertilizer Recommendation System")
st.markdown("Enter your soil and weather conditions below to get AI-based crop and fertilizer suggestions.")

# Input fields
st.header("🧪 Enter Soil and Weather Parameters")
col1, col2, col3 = st.columns(3)

with col1:
    N = st.number_input("Nitrogen (N)", 0, 200, 0)
    P = st.number_input("Phosphorous (P)", 0, 200, 0)

with col2:
    K = st.number_input("Potassium (K)", 0, 200, 0)
    ph = st.number_input("pH level", 0.0, 14.0, 6.5)

with col3:
    temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
    humidity = st.number_input("Humidity (%)", 0.0, 100.0, 50.0)
    rainfall = st.number_input("Rainfall (mm)", 0.0, 400.0, 100.0)

# Predict button
if st.button("Get Recommendations"):
    # Prepare input for crop model
    crop_input = [[N, P, K, temperature, humidity, ph, rainfall]]
    crop_prediction = crop_model.predict(crop_input)
    crop_name = crop_le.inverse_transform(crop_prediction)[0]

    # Prepare input for fertilizer model
    fert_input = [[N, K, P]]  # Match fertilizer dataset order
    fert_prediction = fert_model.predict(fert_input)
    fert_name = fert_le.inverse_transform(fert_prediction)[0]

    # Show results
    st.success(f"🌱 Recommended Crop: **{crop_name}**")
    st.success(f"💊 Recommended Fertilizer: **{fert_name}**")

    st.info("ℹ️ Tip: Apply fertilizers in split doses and ensure proper irrigation for best yield.")

# Footer
st.markdown("---")
st.caption("Developed as an AI-based Internship Project | Machine Learning | Streamlit")
