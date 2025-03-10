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
        FBS = create_input('Fasting Blood Sugar > 120 mg/dl (1=True, 0=False)', 'FBS')
        RestECG = create_input('Resting ECG Results', 'RestECG')

    with col2:
        
        Thalach = create_input('Max Heart Rate', 'Thalach')
        Exang = create_input('Exercise Induced Angina (1=Yes, 0=No)', 'Exang')
        Oldpeak = create_input('ST Depression Induced by Exercise', 'Oldpeak')
        Slope = create_input('Slope of Peak Exercise ST Segment (0, 1, 2)', 'Slope')
        CA = create_input('Major Vessels Colored by Fluoroscopy (0-3)', 'CA')
        Thal = create_input('Thal (0=Normal, 1=Fixed Defect, 2=Reversible Defect)', 'Thal')

    inputs = [Age, Sex, CP, Trestbps, Chol, FBS, RestECG, Thalach, Exang, Oldpeak, Slope, CA, Thal]

elif selected == '🧠 Parkinsons':
    with col1:
        Fo = create_input('MDVP:Fo(Hz)', 'Fo')
        Fhi = create_input('MDVP:Fhi(Hz)', 'Fhi')
        Flo = create_input('MDVP:Flo(Hz)', 'Flo')
        Jitter_percent = create_input('MDVP:Jitter(%)', 'Jitter_percent')
        Jitter_Abs = create_input('MDVP:Jitter(Abs)', 'Jitter_Abs')
        RAP = create_input('MDVP:RAP', 'RAP')
        PPQ = create_input('MDVP:PPQ', 'PPQ')
        DDP = create_input('Jitter:DDP', 'DDP')
        Shimmer = create_input('MDVP:Shimmer', 'Shimmer')
        Shimmer_dB = create_input('MDVP:Shimmer(dB)', 'Shimmer_dB')
        APQ3 = create_input('Shimmer:APQ3', 'APQ3')

    with col2:
        APQ5 = create_input('Shimmer:APQ5', 'APQ5')
        APQ = create_input('MDVP:APQ', 'APQ')
        DDA = create_input('Shimmer:DDA', 'DDA')
        NHR = create_input('NHR', 'NHR')
        HNR = create_input('HNR', 'HNR')
        RPDE = create_input('RPDE', 'RPDE')
        DFA = create_input('DFA', 'DFA')
        Spread1 = create_input('Spread1', 'Spread1')
        Spread2 = create_input('Spread2', 'Spread2')
        D2 = create_input('D2', 'D2')
        PPE = create_input('PPE', 'PPE')

    inputs = [
    float(Fo), float(Fhi), float(Flo),
    float(Jitter_percent), float(Jitter_Abs), float(RAP),
    float(PPQ), float(DDP), float(Shimmer),
    float(Shimmer_dB), float(APQ3), float(APQ5),
    float(APQ), float(DDA), float(NHR),
    float(HNR), float(RPDE), float(DFA),
    float(Spread1), float(Spread2), float(D2), float(PPE)
]

elif selected == '🫁 Lung Cancer':
    with col1:
        GENDER = create_input('Gender (1 = Male; 0 = Female)', 'GENDER')
        AGE = create_input('Age', 'AGE')
        SMOKING = create_input('Smoking (1 = Yes; 0 = No)', 'SMOKING')
        YELLOW_FINGERS = create_input('Yellow Fingers (1 = Yes; 0 = No)', 'YELLOW_FINGERS')
        ANXIETY = create_input('Anxiety (1 = Yes; 0 = No)', 'ANXIETY')
        PEER_PRESSURE = create_input('Peer Pressure (1 = Yes; 0 = No)', 'PEER_PRESSURE')
        CHRONIC_DISEASE = create_input('Chronic Disease (1 = Yes; 0 = No)', 'CHRONIC_DISEASE')
        FATIGUE = create_input('Fatigue (1 = Yes; 0 = No)', 'FATIGUE')

    with col2:
        ALLERGY = create_input('Allergy (1 = Yes; 0 = No)', 'ALLERGY')
        WHEEZING = create_input('Wheezing (1 = Yes; 0 = No)', 'WHEEZING')
        ALCOHOL_CONSUMING = create_input('Alcohol Consuming (1 = Yes; 0 = No)', 'ALCOHOL_CONSUMING')
        COUGHING = create_input('Coughing (1 = Yes; 0 = No)', 'COUGHING')
        SHORTNESS_OF_BREATH = create_input('Shortness Of Breath (1 = Yes; 0 = No)', 'SHORTNESS_OF_BREATH')
        SWALLOWING_DIFFICULTY = create_input('Swallowing Difficulty (1 = Yes; 0 = No)', 'SWALLOWING_DIFFICULTY')
        CHEST_PAIN = create_input('Chest Pain (1 = Yes; 0 = No)', 'CHEST_PAIN')

    inputs = [GENDER, AGE, SMOKING,YELLOW_FINGERS,ANXIETY,PEER_PRESSURE,CHRONIC_DISEASE,FATIGUE,ALLERGY,WHEEZING,ALCOHOL_CONSUMING,COUGHING,SHORTNESS_OF_BREATH,SWALLOWING_DIFFICULTY,CHEST_PAIN]

elif selected == '🔬 Hypo-Thyroid':
    with col1:
        Age = create_input('Age', 'Age')
        Sex= create_input('Sex','Sex')
        TSH = create_input('TSH Level', 'TSH')
        T3 = create_input('T3 Level', 'T3')
    with col2:
        TT4 = create_input('TT4 Level', 'TT4')
        T4U = create_input('T4U Level', 'T4U')
        FTI = create_input('FTI Level', 'FTI')
    inputs = [Age,Sex, TSH, T3, TT4, T4U, FTI]


# Prediction button
if st.button(f'Predict {selected}'):
    model = models[selected]
    prediction = model.predict([inputs])
    result = 'Positive' if prediction[0] == 1 else 'Negative'
    st.success(f'The person is {result} for {selected}')
