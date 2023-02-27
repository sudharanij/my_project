import streamlit as st
from matplotlib import image
import pandas as pd
import seaborn as sns
import plotly.express as px
import os


# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resource")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "download.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Real_estate.csv")

st.title("Dashboard - Real Estate Data")

img = image.imread(IMAGE_PATH)

st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

status = st.selectbox("Select the Status:", df['Status'].unique())


fig_1 = px.histogram(df[df['Status'] == status], x="Location")
st.plotly_chart(fig_1, use_container_width=True)

fig_2 = px.box(df[df['Status'] == status], y="Ppsqft")
st.plotly_chart(fig_2, use_container_width=True)

#fig_3 = sns.countplot(x='Status',data=df)
#st.pyplot(fig_3.figure)