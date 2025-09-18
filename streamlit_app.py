import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="Análisis de Almacenamiento", layout="wide")
st.title("📊 Análisis de Soluciones de Almacenamiento de Datos")

# -------------------------------
# 1. Escenario de la empresa
# -------------------------------
st.header("1️⃣ Descripción del Escenario")
empresa = st.text_input("Nombre de la empresa")
problemas = st.text_area("Problemas de almacenamiento actuales")
objetivos = st.text_area("Objetivos del proyecto")

# -------------------------------
# 2. Criterios de evaluación
# -------------------------------
st.header("2️⃣ Criterios de Evaluación")
criterios = {
    "Velocidad de lectura/escritura": "GB/s, indica rapidez de acceso a los datos",
    "Capacidad total": "TB, espacio disponible de almacenamiento",
    "Costo por GB": "USD/GB, costo económico",
    "Fiabilidad (MTBF)": "Horas, duración promedio antes de fallo",
    "Consumo energético": "kWh, eficiencia energética",
    "Seguridad": "Nivel de cifrado y protección",
    "Escalabilidad": "Facilidad de ampliar capacidad"
}

for criterio, descripcion in criterios.items():
    st.info(f"**{criterio}**: {descripcion}")

# -------------------------------
# 3. Comparación de tecnologías
# -------------------------------
st.header("3️⃣ Comparación de Tecnologías")
data = {
    "Tecnología": ["HDD", "SSD", "Cintas", "Nube"],
    "Velocidad (MB/s)": [150, 550, 50, 300],
    "Capacidad (TB)": [10, 4, 20, 100],
    "Costo por GB (USD)": [0.03, 0.15, 0.01, 0.05],
    "Fiabilidad (MTBF h)": [100000, 150000, 50000, 200000],
    "Consumo energético (W)": [10, 5, 2, 1],
    "Seguridad (1-5)": [3, 4, 2, 5],
    "Escalabilidad (1-5)": [3, 4, 2, 5]
}
df = pd.DataFrame(data)
st.dataframe(df)

# Opción de exportar tabla
st.download_button(
    label="📥 Descargar tabla CSV",
    data=df.to_csv(index=False).encode('utf-8'),
    file_name='comparacion_tecnologias.csv',
    mime='text/csv'
)

# -------------------------------
# 4. Gráficos comparativos
# -------------------------------
st.header("4️⃣ Gráficos Comparativos")

# Gráfico de barras: velocidad
fig1 = px.bar(df, x="Tecnología", y="Velocidad (MB/s)", color="Tecnología", title="Velocidad de lectura/escritura")
st.plotly_chart(fig1, use_container_width=True)

# Gráfico radar: fiabilidad, escalabilidad y seguridad
import plotly.graph_objects as go
fig2 = go.Figure()
fig2.add_trace(go.Scatterpolar(
      r=df.loc[0, ["Fiabilidad (MTBF h)","Escalabilidad (1-5)","Seguridad (1-5)"]],
      theta=["Fiabilidad","Escalabilidad","Seguridad"],
      fill='toself',
      name=df.loc[0, "Tecnología"]
))
fig2.add_trace(go.Scatterpolar(
      r=df.loc[1, ["Fiabilidad (MTBF h)","Escalabilidad (1-5)","Seguridad (1-5)"]],
      theta=["Fiabilidad","Escalabilidad","Seguridad"],
      fill='toself',
      name=df.loc[1, "Tecnología"]
))
fig2.add_trace(go.Scatterpolar(
      r=df.loc[2, ["Fiabilidad (MTBF h)","Escalabilidad (1-5)","Seguridad (1-5)"]],
      theta=["Fiabilidad","Escalabilidad","Seguridad"],
      fill='toself',
      name=df.loc[2, "Tecnología"]
))
fig2.add_trace(go.Scatterpolar(
      r=df.loc[3, ["Fiabilidad (MTBF h)","Escalabilidad (1-5)","Seguridad (1-5)"]],
      theta=["Fiabilidad","Escalabilidad","Seguridad"],
      fill='toself',
      name=df.loc[3, "Tecnología"]
))
fig2.update_layout(polar=dict(radialaxis=dict(visible=True)), showlegend=True)
st.plotly_chart(fig2, use_container_width=True)

# -------------------------------
# 5. Simulación de crecimiento de datos
# -------------------------------
st.header("5️⃣ Simulación de Crecimiento de Datos")
volumen_inicial = st.number_input("Volumen inicial (TB)", value=10)
tasa_crecimiento = st.slider("Tasa de crecimiento anual (%)", 0, 100, 50)
años = st.slider("Número de años", 1, 10, 2)

años_lista = list(range(años+1))
volumen_total = [volumen_inicial * (1 + tasa_crecimiento/100)**i for i in años_lista]

fig3 = px.line(x=años_lista, y=volumen_total, markers=True, title="Crecimiento de Datos")
fig3.update_layout(xaxis_title="Año", yaxis_title="Volumen de datos (TB)")
st.plotly_chart(fig3, use_container_width=True)

# -------------------------------
# 6. Conclusiones
# -------------------------------
st.header("6️⃣ Conclusiones")
st.write("""
- Según los criterios evaluados, la **SSD** ofrece mejor velocidad y fiabilidad para operaciones críticas.
- La **nube** es la opción más escalable y segura.
- Se recomienda una **solución híbrida SSD + Nube** para balancear costo, rendimiento y escalabilidad.
""")
