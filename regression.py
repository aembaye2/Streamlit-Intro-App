
import wooldridge as woo
import streamlit as st
import statsmodels.formula.api as smf
import scipy.stats as stats
import pandas as pd

# load dataset from package:
#wage1 = woo.dataWoo('wage1')

# Write the data to CSV in the codespaces workspace
#wage1.to_csv('wage1.csv', index=False)  # index=False prevents writing row numbers

# Load the dataset from workspace
wage1 = pd.read_csv('wage1.csv')

# Display the first few rows
st.subheader("First 5 Rows of the Dataset")
st.write(wage1.head())

# Display summary statistics
st.subheader("Summary Statistics")
st.write(wage1.describe())

# Doing multiple linear regression:
# store and display results:
reg = smf.ols(formula='wage ~ educ + exper + tenure', data=wage1)
results = reg.fit()
# st.subheader("Regression Summary")
# st.text(results.summary())

st.subheader("Regression Summary (HTML Style)")
st.markdown(results.summary().as_html(), unsafe_allow_html=True)
