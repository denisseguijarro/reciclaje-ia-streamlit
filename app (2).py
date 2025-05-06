
import streamlit as st
import pandas as pd
import joblib

# Cargar el modelo previamente entrenado
model = joblib.load("arbol_decision_reciclaje.pkl")

st.title("Clasificador de Reciclabilidad de Subproductos Químicos")

st.markdown("Introduce las características del subproducto para predecir su potencial de reciclaje.")

# Entradas del usuario
ph = st.number_input("pH", min_value=0.0, max_value=14.0, value=7.0)
temperatura = st.number_input("Temperatura (°C)", value=25.0)
presion = st.number_input("Presión (atm)", value=1.0)
h2so4 = st.number_input("% H2SO4", min_value=0.0, max_value=100.0, value=0.0)

tratamiento = st.selectbox("Tratamiento previo", ["relleno", "reutilizado", "incinerado"])
proceso = st.selectbox("Proceso de origen", [
    "fertilizantes", "tratamiento_agua", "explosivos", "refinado", "textiles",
    "farmacéutica", "pinturas", "minerales", "agroindustria", "plásticos"
])

if st.button("Predecir reciclabilidad"):
    # Crear DataFrame de entrada
    input_df = pd.DataFrame([{
        'pH': ph,
        'temperatura': temperatura,
        'presion': presion,
        'composicion_H2SO4': h2so4,
        'tratamiento_previo': tratamiento,
        'proceso_origen': proceso
    }])

    # Realizar predicción
    resultado = model.predict(input_df)[0]
    st.success(f"El potencial de reciclaje es: **{resultado.upper()}**")
