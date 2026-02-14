import streamlit as st
import joblib
import numpy as np

model = joblib.load("fraud_model.pkl")

st.title("💳 AI Fraud Detection System")

st.write("Enter transaction details:")

# We need 30 features (same as dataset minus Class)
features = []

for i in range(30):
    value = st.number_input(f"Feature {i+1}", value=0.0)
    features.append(value)

if st.button("Check Transaction"):
    input_data = np.array([features])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("⚠ Fraudulent Transaction Detected")
    else:
        st.success("Legitimate Transaction")
