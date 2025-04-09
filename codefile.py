# This are the variables"
# MedInc: Median income in block group.
# HouseAge: Median age of houses in block group.
# AveRooms: Average number of rooms per household.
# AveOccup: Average number of household members.
# Lat: Latitude of the block group.
# Long: Longitude of the block group.
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# Adjust the path based on where the dataset is in your repo
file_path = 'Sample_Data_for_Plotting_and_Filtering.csv'

# Load the dataset
df = pd.read_csv(file_path)

# Now you can work with your DataFrame
st.write(df.head())
