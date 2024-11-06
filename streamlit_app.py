import streamlit as st

st.title('alzheimers_disease')

st.write('my project pridict does person have alzheimers disease or no.')
# app.py
import streamlit as st
import pandas as pd

uploaded_file = st.file_uploader("alzheimers_disease_patient_data", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Ваши данные:")
    st.write(df)
