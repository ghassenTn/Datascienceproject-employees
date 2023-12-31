import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Employee Dashboard",
                   page_icon=':bar_chart',
                   layout="wide",
                   initial_sidebar_state="expanded")
# load data
df = pd.read_csv('notebooks/employee pro')
st.title(' :bar_chart: Employee Dashboard')
st.markdown('<style>div.block-container {padding-top:1rem;}</style>', unsafe_allow_html=True)
# sidebar
st.sidebar.subheader("Tips Dashboard")
st.sidebar.image('assets/people.png', width=200)
st.sidebar.write("This dashboard is using employees dataset from seaborn for educational purposes.")
st.sidebar.write("")
st.sidebar.write("Filter your data:")
chose = st.sidebar.selectbox('choose', options=['sexe', 'specialite', 'degree'])


def plot_gender_count(dataframe):
    gender_counts = dataframe['sexe'].value_counts()
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.bar(gender_counts.index, gender_counts.values)
    ax.set_title('Count of Gender')
    ax.set_xlabel('Gender')
    ax.set_ylabel('Count')
    ax.tick_params(axis='x', rotation=45)  # Rotate x-axis labels for better visibility
    return fig


if chose == 'sexe':
    st.pyplot(plot_gender_count(df))
