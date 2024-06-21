import streamlit as st
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Load data
@st.cache_data
def load_data():
    data = pd.read_csv("House_Price_Prediction/house_prices_train.csv")
    return data

data = load_data()

# Prepare the data
X = data[['num_bedrooms', 'num_bathrooms', 'square_footage', 'age_of_house', 'location']]
X = pd.get_dummies(X, columns=['location'], drop_first=True)  # Convert categorical data to numeric
y = data['price']

# Train the model
model = LinearRegression()
model.fit(X, y)

# Streamlit app
st.title("House Price Prediction")

st.write("""
### Enter the house details to predict the price
""")

# Input features
num_bedrooms = st.number_input("Number of Bedrooms", min_value=1, max_value=10, value=3)
num_bathrooms = st.number_input("Number of Bathrooms", min_value=1, max_value=5, value=2)
square_footage = st.number_input("Square Footage", min_value=500, max_value=5000, value=1500)
age_of_house = st.number_input("Age of the House (years)", min_value=0, max_value=100, value=20)
location = st.selectbox("Location", ['A', 'B', 'C', 'D', 'E'])

# Create a dataframe for the input
input_data = pd.DataFrame({
    'num_bedrooms': [num_bedrooms],
    'num_bathrooms': [num_bathrooms],
    'square_footage': [square_footage],
    'age_of_house': [age_of_house],
    'location': [location]
})

# Convert categorical data to numeric
input_data = pd.get_dummies(input_data, columns=['location'], drop_first=True)
# Ensure the input data has the same columns as the training data
for col in X.columns:
    if col not in input_data.columns:
        input_data[col] = 0

# Predict the price
predicted_price = model.predict(input_data)[0]

st.write(f"The predicted house price is ${predicted_price:,.2f}")
