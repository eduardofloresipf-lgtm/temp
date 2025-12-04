import streamlit as st
import pandas as pd
import pickle

st.image("cl.jpeg", caption="Predicción de temperatura en México")

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Predicción de temperatura en ciudades de México")
st.header("Datos de entrada")

def user_input_features():

    year = st.number_input("Año", min_value=1700, max_value=2100, value=2024)
    month = st.number_input("Mes (1–12)", min_value=1, max_value=12, value=1)

    ciudades = {"Acapulco": 0,
    "Acuña": 1,
    "Aguascalientes": 2,}

    ciudad_nombre = st.selectbox("Ciudad", ciudades)
    ciudad_encoded = ciudad_map[ciudad_nombre]

    user_data = {
        "year": year,
        "month": month,
        "City_encoded": ciudad_encoded
    }

    return pd.DataFrame(user_data, index=[0])

input_df = user_input_features()

if st.button("Predecir temperatura"):
    pred = model.predict(input_df)
    st.success(f"Temperatura estimada: {pred[0]:.2f} °C")
