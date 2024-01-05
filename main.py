import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import base64
from filtre.filtrage import *
from charts.charts import *
st.set_page_config(page_title="Employee Dashboard",
                   page_icon=':bar_chart',
                   layout="wide",
                   initial_sidebar_state="expanded")
# load data
df = pd.read_csv('notebooks/employee pro')
st.sidebar.image('assets/people.png', width=200)
st.sidebar.write("Filter your data:")
specealite = st.sidebar.multiselect('Choose specialty', options=df['specialite'].unique(),
                                    default=df['specialite'].unique())
sexe = st.sidebar.multiselect('Choose gender', options=df['sexe'].unique(), default=df['sexe'].unique())
niveau = st.sidebar.multiselect('Choose level', options=df['diplome'].unique(), default=df['diplome'].unique())
dispo = st.sidebar.multiselect('Choose availability', options=df['dispo'].unique(), default=df['dispo'].unique())
cheuveuxcolor = st.sidebar.multiselect('Choose hair color', options=df['cheveux'].unique(), default=df['cheveux'].unique())
# Display the filtered DataFrame
dffilterd= filtredf(df,specealite,sexe,niveau,dispo,cheuveuxcolor)
st.dataframe(dffilterd)
columns = [col for col in df.columns if col != 'Unnamed: 0' and col!= 'indice']
col_choose = st.sidebar.selectbox('Choisir une colonne', options=columns)

if col_choose:
    # Check if the selected column is 'exp', 'age', 'note', or 'salaire'
    if col_choose:
        # Check if the selected column is 'exp', 'age', 'note', or 'salaire'
        if col_choose in ['exp', 'age', 'note']:
            # Convert float columns to integer
            df[col_choose] = df[col_choose].astype(int)

            # Get the min and max values for the selected column
            min_val = df[col_choose].min()
            max_val = df[col_choose].max()

            # Create a slider to select the interval
            interval = st.sidebar.slider(f"Choisir l'intervalle de {col_choose}", min_val, max_val, (min_val, max_val))

            # Plot value counts within the selected interval
            res = plot_value_counts_within_interval(df, col_choose, interval)
            #st.write(df[col_choose].describe())
            #col_description = df[col_choose].describe()
            st.write(res)

        else:
            # Plot value counts for columns other than 'exp', 'age', 'note', or 'salaire'
            plot_value_counts(df, col_choose)
    else:
        plot_value_counts(df, col_choose)



