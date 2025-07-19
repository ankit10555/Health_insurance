import streamlit as st
from Predicthelper import predict
from joblib import load

st.set_page_config(page_title="Health Insurance Form", layout="wide")
st.title("🩺 Health Insurance Premium Prediction")

with st.form("insurance_form"):
    st.subheader("📝 Enter Customer Details")

    # Row 1: Age, Gender, Region, Marital Status
    col1, col2, col3, col4 = st.columns(4)
    age = col1.number_input("Age", min_value=18, max_value=100, step=1)
    gender = col2.selectbox("Gender", ['Male', 'Female'])
    region = col3.selectbox("Region", ['Northwest', 'Southeast', 'Northeast', 'Southwest'])
    marital_status = col4.selectbox("Marital Status", ['Unmarried', 'Married'])

    # Row 2: BMI Category, Smoking Status, Employment Status, Income Level
    col5, col6, col7, col8 = st.columns(4)
    bmi_category = col5.selectbox("BMI Category", ['Normal', 'Obesity', 'Overweight', 'Underweight'])
    smoking_status = col6.selectbox(
        "Smoking Status",
        ['No Smoking', 'Regular', 'Occasional']
    )
    employment_status = col7.selectbox("Employment Status", ['Salaried', 'Self-Employed', 'Freelancer'])
    genetical_risk=col8.number_input('genetical_risk', min_value=0, max_value=5, step=1)


    # Row 3: Insurance Plan, Medical History, No. of Dependents, Income in Lakhs
    col9, col10, col11, col12 = st.columns(4)
    insurance_plan = col9.selectbox("Insurance Plan", ['Bronze', 'Silver', 'Gold'])
    medical_history = col10.selectbox(
        "Medical History",
        [
            'Diabetes', 'High blood pressure', 'No Disease',
            'Diabetes & High blood pressure', 'Thyroid', 'Heart disease',
            'High blood pressure & Heart disease', 'Diabetes & Thyroid',
            'Diabetes & Heart disease'
        ]
    )
    number_of_dependants = col11.number_input('Number of Dependants', min_value=0, max_value=20, step=1)
    income_lakhs = col12.number_input('Income in Lakhs', min_value=0, max_value=200, step=1)

    # Bottom-right Predict button
    colspacer, colbtn = st.columns([11, 1])
    with colbtn:
        predict_clicked = st.form_submit_button("Predict")

    input_dict={
        "age": age,
        "number_of_dependants": number_of_dependants,
        "income_lakhs": income_lakhs,
        "insurance_plan": insurance_plan,
        "genetical_risk": genetical_risk,
        "medical_history": medical_history,
        "gender": gender,
        "region": region,
        "marital_status": marital_status,
        "bmi_category": bmi_category,
        "smoking_status": smoking_status,
        "employment_status": employment_status,
    }

    if predict_clicked:
        prediction=predict(input_dict)
        st.success(f"Predicted premium:₹{round(prediction[0],0)}")


