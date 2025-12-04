import streamlit as st
import pandas as pd

st.image("cl.jpeg", caption="Predicción de temperatura en México")

st.title("Predicción de temperatura en ciudades de México")
st.header("Datos de entrada")

ciudad_map = {
    "Acapulco": 0,
    "Acuña": 1,
    "Aguascalientes": 2
}

ciudades = list(ciudad_map.keys())

def user_input_features():
    year = st.number_input(
        "Año",
        min_value=1700,
        max_value=2100,
        value=2024,
        step=1
    )

    month = st.number_input(
        "Mes (1–12)",
        min_value=1,
        max_value=12,
        value=1,
        step=1
    )

    ciudad_nombre = st.selectbox("Ciudad", ciudades)
    ciudad_encoded = ciudad_map[ciudad_nombre]

    user_data = {
        "year": year,
        "month": month,
        "City_encoded": ciudad_encoded
    }

    return pd.DataFrame(user_data, index=[0])

input_df = user_input_features()

st.write("Datos de entrada para el modelo:")
st.write(input_df)

if st.button("Predecir temperatura"): pred = model.predict(input_df) st.success(f"Temperatura estimada: {pred[0]:.2f} °C")
