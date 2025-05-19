import streamlit as st
import joblib
import pandas as pd

# Load the optimized model
model = joblib.load('optimized_model.h5')

st.title('Flight Price Prediction App')
st.write('Enter flight details below to get the predicted price.')

# User inputs for flight details
airline = st.selectbox('Select Airline', ['Air India', 'IndiGo', 'Jet Airways'])
source = st.selectbox('Source City', ['Kolkata', 'Delhi', 'Mumbai'])
destination = st.selectbox('Destination City', ['Banglore', 'Cochin', 'Delhi'])
additional_info = st.selectbox('Additional Info', ['No info', 'In-flight meal not included'])

# Encoding user inputs to match model training
encoder = {'Air India': 0, 'IndiGo': 1, 'Jet Airways': 2,
           'Kolkata': 0, 'Delhi': 1, 'Mumbai': 2,
           'Banglore': 0, 'Cochin': 1, 'Delhi': 2,
           'No info': 0, 'In-flight meal not included': 1}

# Preparing input data
input_data = pd.DataFrame([[encoder[airline], encoder[source], encoder[destination], encoder[additional_info]]],
                          columns=['Airline', 'Source', 'Destination', 'Additional_Info'])

# Predicting the price
if st.button('Predict Price'):
    prediction = model.predict(input_data)
    st.success(f'The predicted flight price is: ${round(prediction[0], 2)}')
