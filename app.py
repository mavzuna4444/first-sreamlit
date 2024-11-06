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
  BMI = 
  Smoking = st.selectbox("do you smoke?", [0, 1])
  Alcohol_Consumption = 
  Physical_Activity = 
  DietQuality = 
  Sleep_Quality = st.slider("Часы сна", 0.0, 12.0, 7.0)
  Family_History_Alzheimers = st.selectbox("Does anyone in your family suffer from this disease?", [0, 1])
  Cardiovascular_Disease =  st.selectbox("do you have CardiovascularDisease?", [0, 1])
  Diabetes = st.selectbox("do you have Diabetes?", [0, 1])
  Depression = st.selectbox("do you have Depression?", [0, 1])
  Head_Injury = st.selectbox("do you have Head Injury?", [0, 1])
  Hypertension = st.selectbox("do you have Hypertension?", [0, 1])
  SystolicBP	=
  DiastolicBP = 
  CholesterolTotal = 
  MMSE	=
  FunctionalAssessment	=
  MemoryComplaints	=
  BehavioralProblems	=
  ADL	=
  Confusion	=
  Disorientation	=
  PersonalityChanges	=
  DifficultyCompletingTasks	=
  Forgetfulness	=
  
  technology_usage = st.slider("Часы использования технологий", 0.0, 15.0, 6.0)
  social_media_usage = st.slider("Часы использования социальных сетей", 0.0, 15.0, 3.0)
  gaming_hours = st.slider("Часы на игры", 0.0, 10.0, 1.0)
  screen_time = st.slider("Общее экранное время (часов)", 0.0, 20.0, 8.0)
  physical_activity_hours = st.slider("Часы физической активности", 0.0, 10.0, 3.0)
  support_systems_access = st.selectbox("Доступ к системам поддержки", ["Yes", "No"])
  work_environment_impact = st.selectbox("Влияние рабочей среды", ["Positive", "Negative"])
  online_support_usage = st.selectbox("Использование онлайн-поддержки", ["Yes", "No"])
  stress_level = st.selectbox("Уровень стресса", ["Low", "Medium", "High"])
