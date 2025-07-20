# 🩺 Health Insurance Premium Prediction App

This is a machine learning-powered web application built with **Streamlit** to predict **health insurance premium amounts** based on user input like age, region, income, lifestyle habits, medical history, and more.

---

## 🚀 Live Model deployed at:

Live App: https://ankitraj-healthinsurance-ml.streamlit.app/  


---

## 🧠 Model Overview

Two separate ML models are used:
- `model_adult.joblib` for users **above 25**
- `model_youngs.joblib` for users **25 and below**

Each model predicts the premium based on features such as:
- Age
- Gender
- Region
- Employment Status
- Smoking Habits
- Medical History
- BMI Category
- Income
- Insurance Plan
- Genetical Risk

---

## 📂 Project Structure

health_insurance/
│
├── app/
│ └── artaffect/
│ ├── main.py # Streamlit frontend app
│ ├── Predicthelper.py # Model loading, preprocessing & prediction
│ ├── model_adult.joblib # Model for adults
│ ├── model_youngs.joblib # Model for young customers
│ ├── scalar_adult.joblib # Scaler for adults
│ ├── scalar_youngs.joblib # Scaler for young customers
│
├── requirements.txt # Required Python packages
├── README.md # This file


# Dependencies
streamlit==1.46.1
xgboost==3.0.2
joblib==1.5.1
scikit-learn==1.7.0
pandas==2.3.1
numpy==2.3.1
