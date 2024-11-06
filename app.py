import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('😁 Abubakr First APP')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  st.write("Загрузите файл CSV для анализа")

uploaded_file = st.file_uploader("Выберите файл", type="csv")
if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write("Ваши данные:")
    st.write(df)
  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw
