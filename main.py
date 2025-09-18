import streamlit as st
import pandas as pd

st.title("Análisis de Soluciones de Almacenamiento")

# Sección 1: Escenario
st.header("1. Descripción del Escenario")
empresa = st.text_input("Nombre de la empresa")
problema = st.text_area("Problemas de almacenamiento actuales")

# Sección 2: Tabla de comparación
st.header("2. Comparación de Tecnologías")
data = {
    "Tecnología": ["HDD", "SSD", "Cintas", "Nube"],
    "Velocidad": [100, 500, 50, 300],
    "Capacidad": [1000, 500, 2000, 10000]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Otras secciones se pueden agregar después
