import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import datetime

date_today = datetime.datetime.now().strftime("%m-%d-%Y")
scoresheet_df = pd.read_excel(r'Frontend/scorepredictions.xlsx',sheet_name=f"gamesheet_{date_today}", index_col=[0])


st.title('Football Predictions Across Top 5 Leagues')

st.markdown("""
* **Leagues:** Premier League, Ligue 1, Bundesliga, Serie A, La Liga
* **Data Source:**understat.com            """)

st.sidebar.header("User Input")

sorted_unique_match = sorted(scoresheet_df["Team"].unique())
selected_match = st.sidebar.selectbox('Match',sorted_unique_match)

nation = sorted(scoresheet_df['Nation'].unique())