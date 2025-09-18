import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("random_forest_model.pkl")

# ===================== CUSTOM CSS =====================
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #d9afd9 0%, #97d9e1 100%);
        font-family: 'Arial', sans-serif;
    }
    .title {
        text-align: center;
        font-size: 42px !important;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 25px;
    }
    .sub-title {
        text-align: left;
        font-size: 20px !important;
        color: #2c3e50;
        font-weight: bold;
        margin-bottom: 10px;
    }
    /* Card style for input section */
    .card {
        background-color: #ffffffcc;
        padding: 25px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    /* Button styling */
    .stButton>button {
        background-color: #2c3e50;
        color: white;
        font-size: 18px;
        border-radius: 8px;
        padding: 10px 25px;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #34495e;
        transform: scale(1.05);
    }
    /* Results */
    .result-success {
        font-size: 26px;
        color: #27ae60;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        background-color: #eafaf1;
    }
    .result-error {
        font-size: 26px;
        color: #c0392b;
        font-weight: bold;
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        background-color: #fdecea;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ===================== APP CONTENT =====================
st.markdown("<h1 class='title'>🩺 Diabetes Prediction App</h1>", unsafe_allow_html=True)
st.markdown(
    "<h3 style='text-align: left; color: #2c3e50;'>Fill the details below to check if a person is likely to have <b>Diabetes</b>:</h3>",
    unsafe_allow_html=True
)




# Input section inside a card
# with st.container():
#     st.markdown("<div class='card'>", unsafe_allow_html=True)

    # Create 2 columns
    # 
col1, col2 = st.columns(2)

with col1:
        pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
        glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
        blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
        skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)

with col2:
        insulin = st.number_input("Insulin Level", min_value=0, max_value=900, value=80)
        bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0, format="%.1f")
        dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=3.0, value=0.5, format="%.2f")
        age = st.number_input("Age", min_value=1, max_value=120, value=30)

st.markdown("</div>", unsafe_allow_html=True)

# Collect features
features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

# Prediction button
if st.button("🔍 Predict"):
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.markdown("<p class='result-error'>⚠️ The model predicts: Diabetic</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='result-success'>✅ The model predicts: Not Diabetic</p>", unsafe_allow_html=True)

