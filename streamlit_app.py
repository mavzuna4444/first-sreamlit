import streamlit as st

st.title('alzheimers_disease')

st.write('my project pridict does person have alzheimers disease or no.')
# app.py
import streamlit as st
import pandas as pd

st.title("Мое Streamlit Приложение")

st.write("Загрузите файл CSV для анализа")

uploaded_file = st.file_uploader("Выберите файл", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Ваши данные:")
    st.write(df)
