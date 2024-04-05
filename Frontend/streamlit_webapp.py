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
* **Data Source:** www.understat.com            """)

st.sidebar.header("User Input")

minBTTS = scoresheet_df['BTTS'].min()
maxBTTS = scoresheet_df['BTTS'].max()
minFGH = scoresheet_df['First Goal Home'].min()
maxFGH = scoresheet_df['First Goal Home'].max()
minFGA = scoresheet_df['First Goal Away'].min()
maxFGA = scoresheet_df['First Goal Away'].max()
BTTS_slider = st.sidebar.slider('BTTS',min_value=minBTTS, max_value=maxBTTS, value=[minBTTS, maxBTTS])
FGH_slider = st.sidebar.slider('First Goal Home',min_value=minFGH, max_value=maxFGH, value=[minFGH, maxFGH])
FGA_slider = st.sidebar.slider('First Goal Away',min_value=minFGA, max_value=maxFGA, value=[minFGA, maxFGA])

nation = sorted(scoresheet_df['Nation'].unique())
selected_nation = st.sidebar.multiselect('Nation',nation,nation)

scoresheet_df_filt = scoresheet_df[(scoresheet_df.Nation.isin(selected_nation)) & (scoresheet_df["BTTS"] >= BTTS_slider[0]) & (scoresheet_df["BTTS"] <= BTTS_slider[1]) & (scoresheet_df["First Goal Home"] >= FGH_slider[0]) & (scoresheet_df["First Goal Home"] <= FGH_slider[1]) & (scoresheet_df["First Goal Away"] >= FGA_slider[0]) & (scoresheet_df["First Goal Away"] <= FGA_slider[1])].copy()

st.header('Predictions this week:')
st.dataframe(scoresheet_df_filt)

