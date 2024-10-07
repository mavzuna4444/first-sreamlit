import streamlit as st

st.title('alzheimers_disease')

st.write('my project pridict does person have alzheimers disease or no.')

import streamlit as st
import pandas as pd

with st.expander('alzheimers_disease_patient_data.csv'):
  df = pd.read_csv('https://www.kaggle.com/datasets/sulimanabusamak123/alzheimers-public-dataset.csv')
  
  del(df['DoctorInCharge'])
  st.write('**X**')
  X_raw = df.drop('Diagnosis', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.Diagnosis
  y_raw

with st.expander('Data visualization'):
  st.scatter_chart(data=df, x='bill_length_mm', y='body_mass_g', color='species')
  st.scatter_chart(data=df, x='bill_depth_mm', y='sex', color='species')
