import streamlit as st
import joblib

model = joblib.load("regression.joblib")

with st.form(key='house_form'):
    size = st.number_input("Enter the size of the house", min_value=0, step=1)

    bedrooms = st.number_input("Enter the number of bedrooms", min_value=0, step=1)

    garden = st.number_input("Does the house have a garden? (0 for No, 1 for Yes)", min_value=0, max_value=1, step=1)

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    prediction = model.predict([[size, bedrooms, garden]])
    if prediction[0] < 0:
        st.write("The estimated price of the house is: 0")
    else:
        st.write(f"The estimated price of the house is: {prediction[0]}")
