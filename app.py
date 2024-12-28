import streamlit as st
import joblib
import numpy as np
from pathlib import Path
from Wine_Quality.pipeline.prediction import PredictionPipeline


def main():
    st.title("Wine Quality Prediction")

    fixed_acidity = st.number_input("Fixed Acidity", min_value=4.0, max_value=15.0, value=7.4, step=0.1)
    volatile_acidity = st.number_input("Volatile Acidity", min_value=0.1, max_value=1.5, value=0.3, step=0.1)
    citric_acid = st.number_input("Citric Acid", min_value=0.0, max_value=1.0, value=0.3, step=0.1)
    residual_sugar = st.number_input("Residual Sugar", min_value=0.0, max_value=15.0, value=2.0, step=0.1)
    chlorides = st.number_input("Chlorides", min_value=0.01, max_value=0.2, value=0.04, step=0.01)
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=1, max_value=80, value=15, step=1)
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=6, max_value=200, value=45, step=1)
    density = st.number_input("Density", min_value=0.98, max_value=1.1, value=0.99, step=0.01)
    pH = st.number_input("pH", min_value=2.5, max_value=4.5, value=3.3, step=0.1)
    sulphates = st.number_input("Sulphates", min_value=0.3, max_value=2.0, value=0.7, step=0.1)
    alcohol = st.number_input("Alcohol", min_value=8.0, max_value=15.0, value=10.0, step=0.1)

    if st.button("Predict Wine Quality"):
        data = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                         free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]).reshape(1, -1)
        
        obj = PredictionPipeline()
        predict = obj.predict(data)

        st.write(f"Predicted Wine Quality: {predict[0]}")

if __name__ == "__main__":
    main()
