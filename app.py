import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

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

# Input features
with st.sidebar:
  st.header('Input features')
  Age = st.number_input("Age", min_value=18, max_value=100, value=25)
  Gender	=  st.selectbox("Gender	", ["Male", "Female"])
  BMI = st.number_input("BMI", min_value=10, max_value=40, value=25)
  Smoking = st.selectbox("do you smoke?", [0, 1])
  Alcohol_Consumption = st.number_input("Alcohol Consumption (years)", min_value=0, max_value=70, value=25)
  Physical_Activity = st.slider("Physical Activit (hours)", 0.0, 10.0, 3.0)
  Diet_Quality =  st.number_input(" Diet Quality", min_value=0, max_value=10, value=25)
  Sleep_Quality = st.slider("how many hours do you sleep?", 0.0, 12.0, 7.0)
  Family_History_Alzheimers = st.selectbox("Does anyone in your family suffer from this disease?", [0, 1])
  Cardiovascular_Disease =  st.selectbox("do you have CardiovascularDisease?", [0, 1])
  Diabetes = st.selectbox("do you have Diabetes?", [0, 1])
  Depression = st.selectbox("have you ever had Depression?", [0, 1])
  Head_Injury = st.selectbox("have you ever had Head Injury?", [0, 1])
  Hypertension = st.selectbox("do you have Hypertension?", [0, 1])
  SystolicBP	= st.number_input("SystolicBP", min_value=90, max_value=200, value=25)
  DiastolicBP = st.number_input("DiastolicBP", min_value=60, max_value=150, value=25)
  Cholesterol_Total = st.number_input("Cholesterol Tota", min_value=150, max_value=400, value=25)
  MMSE	= st.number_input("Mini-Mental State Examination", min_value=0, max_value=30, value=25)
  Functional_Assessment	= st.number_input("Functional Assessment", min_value=0, max_value=10, value=25)
  Memory_Complaints	= st.selectbox("do you have Memory Complaints?", [0, 1])
  Behavioral_Problems	= st.selectbox("do you have Behavioral Problems?", [0, 1])
  ADL	= st.number_input("Activity of Daily Living", min_value=0, max_value=10, value=25)
  Confusion	= st.selectbox("have you ever mixed things up0?", [0, 1])
  Disorientation	= st.selectbox("have you ever experienced Disorientation?", [0, 1])
  Personality_Changes	= st.selectbox("have you ever had a Personality Changes?", [0, 1])
  Difficulty_Completing_Tasks	= st.selectbox("have you ever had a Difficulty Completing Tasks?", [0, 1])
  Forgetfulness	= st.selectbox("do you have Forgetfulness?", [0, 1])
  
