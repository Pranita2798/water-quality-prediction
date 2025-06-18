import streamlit as st
import pandas as pd
import pickle

# Load model
model = pickle.load(open('models/model.pkl', 'rb'))

st.title("💧 Water Quality Index Prediction App")

# Inputs
ph = st.number_input("pH Level", min_value=0.0, max_value=14.0, step=0.1)
do = st.number_input("Dissolved Oxygen (mg/L)", min_value=0.0, step=0.1)
turbidity = st.number_input("Turbidity (NTU)", min_value=0.0, step=0.1)

if st.button("Predict"):
    input_df = pd.DataFrame([[ph, do, turbidity]], columns=['ph', 'do', 'turbidity'])
    prediction = model.predict(input_df)[0]
    proba = model.predict_proba(input_df).max()
    
    st.success(f"Predicted Water Quality Class: **{prediction}**")
    st.info(f"Confidence: {proba:.2%}")
