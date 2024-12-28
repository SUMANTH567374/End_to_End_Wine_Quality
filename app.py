import streamlit as st
import joblib
import numpy as np
from pathlib import Path
from Wine_Quality.pipeline.prediction import PredictionPipeline

def main():
    st.title("Wine Quality Prediction")

    # Using integer values for inputs
    fixed_acidity = st.number_input("Fixed Acidity", min_value=4, max_value=15, value=7, step=1, format="%d")
    volatile_acidity = st.number_input("Volatile Acidity", min_value=1, max_value=15, value=3, step=1, format="%d")
    citric_acid = st.number_input("Citric Acid", min_value=0, max_value=10, value=3, step=1, format="%d")
    residual_sugar = st.number_input("Residual Sugar", min_value=0, max_value=15, value=2, step=1, format="%d")
    chlorides = st.number_input("Chlorides", min_value=1, max_value=20, value=4, step=1, format="%d")
    free_sulfur_dioxide = st.number_input("Free Sulfur Dioxide", min_value=1, max_value=80, value=15, step=1, format="%d")
    total_sulfur_dioxide = st.number_input("Total Sulfur Dioxide", min_value=6, max_value=200, value=45, step=1, format="%d")
    density = st.number_input("Density", min_value=1, max_value=10, value=2, step=1, format="%d")
    pH = st.number_input("pH", min_value=2, max_value=5, value=3, step=1, format="%d")
    sulphates = st.number_input("Sulphates", min_value=1, max_value=20, value=7, step=1, format="%d")
    alcohol = st.number_input("Alcohol", min_value=8, max_value=15, value=10, step=1, format="%d")

    if st.button("Predict Wine Quality"):
        # Collecting inputs into an array
        data = np.array([fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides,
                         free_sulfur_dioxide, total_sulfur_dioxide, density, pH, sulphates, alcohol]).reshape(1, -1)
        
        # Using the PredictionPipeline class for prediction
        obj = PredictionPipeline()
        predict = obj.predict(data)

        # Round the predicted value to the nearest integer
        predicted_quality = round(predict[0])

        # Ensure the prediction is within the expected wine quality range (1 to 10)
        predicted_quality = max(1, min(predicted_quality, 10))

        st.write(f"Predicted Wine Quality: {predicted_quality}")

if __name__ == "__main__":
    main()
