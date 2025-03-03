
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

# # Load the California Housing data
# california = fetch_california_housing()

# # Create a DataFrame
# df = pd.DataFrame(california.data, columns=california.feature_names)

# # Add the target variable (house values)
# df['MedHouseVal'] = california.target

# # Streamlit app
# st.title('California Housing Data Analysis')

# # Show the first few rows of the DataFrame
# st.subheader('First few rows of the dataset:')
# st.write(df.head())

# # Select variables for plotting
# x = df['MedInc'].values.reshape(-1, 1)  # Reshape to 2D array for sklearn
# y = df['MedHouseVal']

# # Fit the linear regression model
# regressor = LinearRegression()
# regressor.fit(x, y)

# # Get the regression results
# slope = regressor.coef_[0]
# intercept = regressor.intercept_
# r_squared = regressor.score(x, y)

# # Show regression output
# st.subheader('Regression Output')
# st.write(f"**Slope (Coefficient of Median Income):** {slope:.4f}")
# st.write(f"**Intercept (Constant):** {intercept:.4f}")
# st.write(f"**R-squared value:** {r_squared:.4f}")

# # Scatterplot with regression line
# st.subheader('Scatterplot of Median Income vs. Median House Value')

# # Create the plot
# plt.figure(figsize=(8, 6))
# sns.regplot(x=df['MedInc'], y=df['MedHouseVal'], scatter_kws={'s': 10}, line_kws={'color': 'red', 'lw': 2})

# # Titles and labels
# plt.title('Scatterplot of Median Income vs. Median House Value', fontsize=16)
# plt.xlabel('Median Income', fontsize=12)
# plt.ylabel('Median House Value (in 100k)', fontsize=12)

# # Show the plot in Streamlit
# st.pyplot(plt)

