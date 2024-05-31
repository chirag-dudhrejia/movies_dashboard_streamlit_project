import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# fetching movies data
md = pd.read_csv("Cleaned_movies_data.csv")


st.set_page_config(page_title="Movie Analytics Dashboard", page_icon="", layout="wide")

st.title("Analytics Dashboard")

# choosing analysis type
st.sidebar.title("Filter")
option = st.sidebar.selectbox("Analysis Type", ["Overall", "Artist", "Director", "Genre", "Year"])

# providing analysis based on option choose
if option == "Overall":
    pass
elif option == "Artist":
    pass
elif option == "Director":
    pass
elif option == "Genre":
    pass
elif option == "Year":
    pass