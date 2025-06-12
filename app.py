import streamlit as st
import pandas as pd
import joblib

st.set_page_config(page_title="Retail Demand Forecasting")
st.title("🛒 Retail Demand Forecasting")

# Load the model
model = joblib.load('model.pkl')

st.markdown("Fill the details below to predict **Weekly Sales**:")

store = st.number_input("Store (as integer label)", min_value=0)
dept = st.number_input("Dept (as integer label)", min_value=0)
date = st.number_input("Date (as integer label)", min_value=0)
isholiday = st.selectbox("Is Holiday", [0, 1])  # 0 = No, 1 = Yes

if st.button("Predict Sales"):
    input_df = pd.DataFrame([[store, dept, date, isholiday]],
                            columns=['Store', 'Dept', 'Date', 'IsHoliday'])
    prediction = model.predict(input_df)[0]
    st.success(f"📦 Predicted Weekly Sales: ₹ {prediction:.2f}")