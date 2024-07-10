import streamlit as st
import requests

first_input = st.number_input("Pick a number " , 0,10)
third_input = st.number_input("Pick a numbers ", 0, 10)
second_input = st.slider("Pick a number ", 0, 10)
fourth_input = st.slider("Pick a numbersss ", 0, 10)

data = [first_input, second_input, third_input, fourth_input]

button = st.button("PREDICT")

if button:

    url = "http://0.0.0.0:9000/predict"
    response = requests.post(url, json=data)

    if response.status_code == 200:
        prediction = response.json().get("prediction")
        print(f"Prediction: {prediction}")
        st.write(f"Prediction: {prediction}")
    else:
        print(f"Request failed with status code {response.status_code}")
        print(f"Response content: {response.content}")
