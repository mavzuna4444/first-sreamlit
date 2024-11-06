import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

st.title('😁 Abubakr First APP')

st.info('This is app builds a machine learning model!')

with st.expander('Data'):
  url = "https://www.kaggle.com/datasets/sulimanabusamak123/alzheimers-public-dataset/code"
  df = pd.read_csv(url)  
  st.write('**X**')
  X_raw = df.drop('species', axis=1)
  X_raw

  st.write('**y**')
  y_raw = df.species
  y_raw
