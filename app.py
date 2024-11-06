import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import BaggingClassifier

st.title('😁 Abubakr First APP')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  df = pd.read_csv('alzheimers_disease_patient_data.csv')  
  del(df['PatientID'])
  del(df['DoctorInCharge'])
  del(df['CholesterolLDL'])
  del(df['CholesterolHDL'])
  del(df['CholesterolTriglycerides'])
  del(df['Ethnicity'])
  del(df['EducationLevel'])

  df
  
  st.write('**X**')
  X_raw = df.drop('Diagnosis', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.Diagnosis
  y_raw

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='Age', y='Diagnosis', color='species')
  st.scatter_chart(data=df, x='Gender', y='Diagnosis', color='species')

# Input features
with st.sidebar:
  st.header('Input features')
  Age = st.number_input("Age", min_value=18, max_value=100, value=25)
  Gender	=  st.selectbox("Gender	(Female=0, Male=1)", [0,1])
  BMI = st.number_input("BMI", min_value=10, max_value=40, value=25)
  Smoking = st.selectbox("do you smoke? (yes=1, no=0)", [0, 1])
  Alcohol_Consumption = st.number_input("Alcohol Consumption (years)", min_value=0, max_value=70, value=25)
  Physical_Activity = st.slider("Physical Activit (hours)", 0.0, 10.0, 3.0)
  Diet_Quality =  st.number_input(" Diet Quality", min_value=0, max_value=10, value=5)
  Sleep_Quality = st.slider("how many hours do you sleep?", 0.0, 12.0, 7.0)
  Family_History_Alzheimers = st.selectbox("Does anyone in your family suffer from this disease? (yes=1, no=0)", [0, 1])
  Cardiovascular_Disease =  st.selectbox("do you have CardiovascularDisease? (yes=1, no=0)", [0, 1])
  Diabetes = st.selectbox("do you have Diabetes? (yes=1, no=0)", [0, 1])
  Depression = st.selectbox("have you ever had Depression? (yes=1, no=0)", [0, 1])
  Head_Injury = st.selectbox("have you ever had Head Injury? (yes=1, no=0)", [0, 1])
  Hypertension = st.selectbox("do you have Hypertension? (yes=1, no=0)", [0, 1])
  SystolicBP	= st.number_input("SystolicBP", min_value=90, max_value=200, value=140)
  DiastolicBP = st.number_input("DiastolicBP", min_value=60, max_value=150, value=100)
  Cholesterol_Total = st.number_input("Cholesterol Tota", min_value=150, max_value=400, value=200)
  MMSE	= st.number_input("Mini-Mental State Examination", min_value=0, max_value=30, value=25)
  Functional_Assessment	= st.number_input("Functional Assessment", min_value=0, max_value=10, value=5)
  Memory_Complaints	= st.selectbox("do you have Memory Complaints? (yes=1, no=0)", [0, 1])
  Behavioral_Problems	= st.selectbox("do you have Behavioral Problems? (yes=1, no=0)", [0, 1])
  ADL	= st.number_input("Activity of Daily Living", min_value=0, max_value=10, value=5)
  Confusion	= st.selectbox("have you ever mixed things up0? (yes=1, no=0)", [0, 1])
  Disorientation	= st.selectbox("have you ever experienced Disorientation? (yes=1, no=0)", [0, 1])
  Personality_Changes	= st.selectbox("have you ever had a Personality Changes? (yes=1, no=0)", [0, 1])
  Difficulty_Completing_Tasks	= st.selectbox("have you ever had a Difficulty Completing Tasks? (yes=1, no=0)", [0, 1])
  Forgetfulness	= st.selectbox("do you have Forgetfulness? (yes=1, no=0)", [0, 1])
  
  #dataFrame
  input_data = pd.DataFrame({'Age': [Age], 	
         'Gender': [Gender], 
         'BMI': [BMI],	
         'Smoking': [Smoking],	
         'Alcohol Consumption': [Alcohol_Consumption], 	
         'Physical Activity': [Physical_Activity],	
         'Diet Quality': [Diet_Quality],
         'Sleep Quality': [Sleep_Quality], 
         'Family_History_Alzheimers': [Family_History_Alzheimers],
         'Cardiovascular Disease': [Cardiovascular_Disease],
         'Diabetes': [Diabetes],
         'Depression': [Depression],
         'Head Injury': [Head_Injury],
         'Hypertension': Hypertension,
         'SystolicBP': [SystolicBP],
         'DiastolicBP': 	[DiastolicBP],
         'Cholesterol Total': [Cholesterol_Total],
         'MMSE': [MMSE],
         'Functional Assessment': [Functional_Assessment],
         'Memory Complaints': [Memory_Complaints],
         'Behavioral Problems': [Behavioral_Problems],
         'ADL': [ADL],
         'Confusion': [Confusion],
         'Disorientation': [Disorientation],
         'Personality Changes':	[Personality_Changes],
         'Difficulty Completing Tasks': [Difficulty_Completing_Tasks],
         'Forgetfulness':	[Forgetfulness]})
  X = input_data[1:]
  input_row = input_data[:1]
  
  # Encode y
  target_mapper = {'not alzheimer': 0,
                 'alzheimer': 1}
  def target_encode(val):
  return target_mapper[val]
  
  y = y_raw.apply(target_encode)
  
  # Model training and inference
  ## Train the ML model
  clf = BaggingClassifier()
  clf.fit(X, y)

  ## Apply model to make predictions
  prediction = clf.predict(input_row)
  prediction_proba = clf.predict_proba(input_row)

  df_prediction_proba = pd.DataFrame(prediction_proba)
  df_prediction_proba.columns = ['not alzheimer', 'alzheimer']
  df_prediction_proba.rename(columns={0: 'not alzheimer',
                                      1: 'alzheimer'})
  st.subheader('Predicted Species')
  st.dataframe(df_prediction_proba,
             column_config={
               'alzheimer': st.column_config.ProgressColumn(
                 'alzheimer',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
               'not alzheimer': st.column_config.ProgressColumn(
                 'not alzheimer',
                 format='%f',
                 width='medium',
                 min_value=0,
                 max_value=1
               ),
             }, hide_index=True)
penguins_species = np.array(['not alzheimer', 'alzheimer'])
st.success(str(penguins_species[prediction][0]))
