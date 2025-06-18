import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open('models/model.pkl', 'rb'))

st.title("💧 Water Quality Index Prediction")

# Input sliders
ph = st.number_input("pH")
do = st.number_input("Dissolved Oxygen (mg/L)")
turbidity = st.number_input("Turbidity (NTU)")

if st.button("Predict"):
    input_df = pd.DataFrame([[ph, do, turbidity]], columns=['ph', 'do', 'turbidity'])
    prediction = model.predict(input_df)[0]
    st.success(f"Predicted Water Quality Class: {prediction}")
