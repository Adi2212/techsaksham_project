import streamlit as st
import pickle
from streamlit_option_menu import option_menu

# Set up the page
st.set_page_config(page_title="Disease Prediction", page_icon="⚕️", layout="wide")

# Apply background using CSS
page_bg = """
<style>
    body {
        background-image: url("https://img.freepik.com/free-vector/hand-drawn-international-nurses-day-background_23-2149341238.jpg?t=st=1741419393~exp=1741422993~hmac=5f6472f9bc311810f96de34e27905fe499b49db2eb70ec70f208d630a0fbffd7&w=1380");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stApp {
        background: rgba(0, 0, 0, 0.6);  /* Adds a dark overlay */
        padding: 20px;
        border-radius: 15px;
    }
    .stMarkdown h1 {
        text-align: center;
        color: white;
        background: linear-gradient(45deg, #28a745, #218838);
        padding: 1rem;
        border-radius: 15px;
    }
</style>
"""
st.markdown(page_bg, unsafe_allow_html=True)

# Load models
models = {
    '🩺 Diabetes': pickle.load(open('./Models/diabetes_model.sav', 'rb')),
    '❤️ Heart Disease': pickle.load(open('./Models/heart_disease_model.sav', 'rb')),
    '🧠 Parkinsons': pickle.load(open('./Models/parkinsons_model.sav', 'rb')),
    '🫁 Lung Cancer': pickle.load(open('./Models/lungs_disease_model.sav', 'rb')),
    '🔬 Hypo-Thyroid': pickle.load(open('./Models/Thyroid_model.sav', 'rb'))
}


# Page Title
st.markdown("<h1>🏥 Disease Prediction System</h1>", unsafe_allow_html=True)

# Select Disease
selected = st.selectbox("Select Disease to Predict", list(models.keys()), index=0)

# Function to create inputs
def create_input(label, key):
    return st.number_input(label, key=key, step=1.0, format="%f")

# Layout for inputs
col1, col2 = st.columns(2)

if selected == '🩺 Diabetes':
    with col1:
        Pregnancies = create_input('Number of Pregnancies', 'Pregnancies')
        Glucose = create_input('Glucose Level', 'Glucose')
        BloodPressure = create_input('Blood Pressure', 'BloodPressure')
        SkinThickness = create_input('Skin Thickness', 'SkinThickness')
    with col2:
        Insulin = create_input('Insulin Level', 'Insulin')
        BMI = create_input('BMI Value', 'BMI')
        DiabetesPedigreeFunction = create_input('Diabetes Pedigree Function', 'DiabetesPedigreeFunction')
        Age = create_input('Age', 'Age')
    inputs = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]

elif selected == '❤️ Heart Disease':
    with col1:
        Age = create_input('Age', 'Age')
        Sex = create_input('Sex (1=Male, 0=Female)', 'Sex')
        CP = create_input('Chest Pain Type', 'CP')
        Trestbps = create_input('Resting Blood Pressure', 'Trestbps')
        Chol = create_input('Cholesterol Level', 'Chol')
    with col2:
        FBS = create_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)', 'FBS')
        RestECG = create_input('Resting ECG Results', 'RestECG')
        Thalach = create_input('Max Heart Rate', 'Thalach')
        Exang = create_input('Exercise Induced Angina (1=Yes, 0=No)', 'Exang')
    inputs = [Age, Sex, CP, Trestbps, Chol, FBS, RestECG, Thalach, Exang]

elif selected == '🧠 Parkinsons':
    with col1:
        MDVP_Fo = create_input('MDVP:Fo(Hz)', 'MDVP_Fo')
        MDVP_Fhi = create_input('MDVP:Fhi(Hz)', 'MDVP_Fhi')
        MDVP_Flo = create_input('MDVP:Flo(Hz)', 'MDVP_Flo')
    with col2:
        Jitter = create_input('Jitter(%)', 'Jitter')
        Shimmer = create_input('Shimmer(%)', 'Shimmer')
        HNR = create_input('HNR', 'HNR')
    inputs = [MDVP_Fo, MDVP_Fhi, MDVP_Flo, Jitter, Shimmer, HNR]

elif selected == '🫁 Lung Cancer':
    with col1:
        Age = create_input('Age', 'Age')
        Smoking = create_input('Smoking (1=Yes, 0=No)', 'Smoking')
        Yellow_Fingers = create_input('Yellow Fingers (1=Yes, 0=No)', 'Yellow_Fingers')
    with col2:
        Anxiety = create_input('Anxiety (1=Yes, 0=No)', 'Anxiety')
        Peer_Pressure = create_input('Peer Pressure (1=Yes, 0=No)', 'Peer_Pressure')
        Chronic_Disease = create_input('Chronic Disease (1=Yes, 0=No)', 'Chronic_Disease')
    inputs = [Age, Smoking, Yellow_Fingers, Anxiety, Peer_Pressure, Chronic_Disease]

elif selected == '🔬 Hypo-Thyroid':
    with col1:
        Age = create_input('Age', 'Age')
        TSH = create_input('TSH Level', 'TSH')
        T3 = create_input('T3 Level', 'T3')
    with col2:
        TT4 = create_input('TT4 Level', 'TT4')
        T4U = create_input('T4U Level', 'T4U')
        FTI = create_input('FTI Level', 'FTI')
    inputs = [Age, TSH, T3, TT4, T4U, FTI]

# Prediction button
if st.button(f'Predict {selected}'):
    model = models[selected]
    prediction = model.predict([inputs])
    result = 'Positive' if prediction[0] == 1 else 'Negative'
    st.success(f'The person is {result} for {selected}')
