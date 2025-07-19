import pandas as pd
import os
from joblib import load

script_directory = os.path.dirname(os.path.abspath(__file__))
print(script_directory) # Keep this for verification if you like, remove later

# Construct the full paths to your model files
model_adult_path = os.path.join(script_directory, "model_adult.joblib")
model_young_path = os.path.join(script_directory, "model_youngs.joblib")

# Load the models using the constructed absolute paths
model_adult = load(model_adult_path)
model_young = load(model_young_path)
print("Both models loaded successfully!")
scalar_adult_path = os.path.join(script_directory, "scalar_adult.joblib")
scalar_young_path = os.path.join(script_directory, "scalar_youngs.joblib")
scalar_adult = load(scalar_adult_path)
scalar_young = load(scalar_young_path)
def calculate_normalised_risk(medical_history):
    risk_score={
        'diabetes':6,
        'high blood pressure':6,
        'no disease':0,
        'thyroid':5,
        'heart disease':8,
        'none':0
    }
    diseases=[disease.strip().lower() for disease in medical_history.split('&')]
    total_risk=sum(risk_score.get(disease,0) for disease in diseases)
    max_score=14
    min_score=0
    normalised_score=total_risk-min_score/(max_score-min_score)
    return normalised_score

def handle_scaling(age,df):
    if age<25:
        scalar_object=scalar_young
    else:
        scalar_object=scalar_adult

    cols_to_scale=scalar_object['cols_to_scale']
    scalar=scalar_object['scalar']
    df["income_level"]=None
    df[cols_to_scale]=scalar.transform(df[cols_to_scale])
    df.drop("income_level",axis=1,inplace=True)
    return df


def preprocessing_input(input_dict):
    expected_columns=['age', 'number_of_dependants', 'income_lakhs', 'insurance_plan',
       'genetical_risk', 'normalised_risk_score', 'gender_Male',
       'region_Northwest', 'region_Southeast', 'region_Southwest',
       'marital_status_Unmarried', 'bmi_category_Obesity',
       'bmi_category_Overweight', 'bmi_category_Underweight',
       'smoking_status_Occasional', 'smoking_status_Regular',
       'employment_status_Salaried', 'employment_status_Self-Employed']

    insurance_plan_encoding={'Bronze':1,'Silver':2,'Gold':3}
    df=pd.DataFrame(0,columns=expected_columns,index=[0])
    for key,value in input_dict.items():
        if key=="gender":
            if value=="Male":
                df['gender_Male']=1
        elif key=="region":
            if value=="Northwest":
                df['region_Northwest']=1
            elif value=="Southeast":
                df['region_Southeast']=1
            elif value=="Southwest":
                df['region_Southwest']=1
        elif key == "marital_status" and value=="Unmarried":
            df['marital_status_Unmarried']=1
        elif key=="bmi_category":
            if value=="Obesity":
                df['bmi_category_Obesity']=1
            elif value=="Overweight":
                df['bmi_category_Overweight']=1
            elif value=="Underweight":
                df['bmi_category_Underweight']=1
        elif key == "smoking_status":
            if value == "Occasional":
                df['smoking_status_Occasional'] = 1
            elif value == "Regular":
                df['smoking_status_Regular'] = 1

        elif key == "employment_status":
            if value == "Salaried":
                df['employment_status_Salaried'] = 1
            elif value == "Self-Employed":
                df['employment_status_Self-Employed'] = 1

        elif key=="age":
            df["age"]=value

        elif key=="number_of_dependants":
            df["number_of_dependants"]=value

        elif key=="income_lakhs":
            df["income_lakhs"]=value

        elif key=="genetical_risk":
            df["genetical_risk"]=value

    df["insurance_plan"] = insurance_plan_encoding.get(input_dict["insurance_plan"], 1)

    df['normalised_risk_score']=calculate_normalised_risk(input_dict["medical_history"])
    handle_scaling(input_dict['age'], df)
    return df





print("Both scalars loaded successfully!")
def predict(input_dict):
    input_df=preprocessing_input(input_dict)
    if input_dict["age"]<=25:
        prediction=model_young.predict(input_df)
    else:
        prediction=model_adult.predict(input_df)

    return prediction






print(type(scalar_adult))
