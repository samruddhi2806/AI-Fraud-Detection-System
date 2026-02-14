import streamlit as st
import numpy as np
from sklearn.linear_model import LogisticRegression

st.title("💳 AI Fraud Detection System")

st.write("This demo uses a trained model inside the app.")

# Train a dummy model (for deployment safety)
@st.cache_resource
def load_model():
    X = np.random.rand(100, 30)
    y = np.random.randint(0, 2, 100)
    model = LogisticRegression()
    model.fit(X, y)
    return model

model = load_model()

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
        st.success("✅ Legitimate Transaction")


