import streamlit as st
import numpy as np
import joblib

# Load model
model = joblib.load("random_forest_model.pkl")

# Apply custom CSS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to right, #e0f7fa, #fce4ec);
    }
    h1 {
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
    }
    h3 {
        color: #34495e;
        margin-bottom: -10px;
    }
    div.stButton > button {
        background-color: #2ecc71;
        color: white;
        font-size: 18px;
        font-weight: bold;
        border-radius: 10px;
        padding: 0.5em 1em;
        transition: 0.3s;
    }
    div.stButton > button:hover {
        background-color: #27ae60;
        transform: scale(1.05);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App title
st.title("🩺 Diabetes Prediction App")
st.markdown("### Fill the details below:")

# Split layout
col1, col2 = st.columns(2)

with col1:
    pregnancies = st.slider("Pregnancies", min_value=0, max_value=20, value=3, step=1)
    glucose = st.slider("Glucose Level", min_value=0, max_value=300, value=120, step=5)
    blood_pressure = st.slider("Blood Pressure", min_value=0, max_value=200, value=70, step=2)
    skin_thickness = st.slider("Skin Thickness", min_value=0, max_value=100, value=20, step=2)

with col2:
    insulin = st.slider("Insulin Level", min_value=0, max_value=900, value=80, step=10)
    age = st.slider("Age", min_value=1, max_value=120, value=30, step=1)
    bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, step=0.1, format="%.1f")
    dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, step=0.01, format="%.2f")

# Features
features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

# Prediction
if st.button("Predict"):
    prediction = model.predict(features)
    probability = model.predict_proba(features)[0][1]

    if prediction[0] == 1:
        st.error(f"⚠️ The model predicts: **Diabetic** ({probability*100:.2f}% confidence)")
    else:
        st.success(f"✅ The model predicts: **Not Diabetic** ({(1-probability)*100:.2f}% confidence)")
