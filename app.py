import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="EDA de Pedidos", layout="centered")

@st.cache_data
def cargar_datos():
    return pd.read_csv("pedidos_limpio.csv")

df = cargar_datos()

st.title("📦 Análisis Exploratorio de Pedidos")
st.markdown("Esta aplicación te permite explorar visualmente los pedidos registrados en tu base de datos.")

# Vista previa
t = st.checkbox("Mostrar primeras filas")
if t:
    st.subheader("👀 Vista previa del dataset")
    st.dataframe(df.head())

# Información básica
st.subheader("📐 Estructura del dataset")
st.write(f"Número de filas: {df.shape[0]}")
st.write(f"Número de columnas: {df.shape[1]}")
st.write("Tipos de datos:")
st.write(df.dtypes)

# Valores nulos
st.subheader("🧩 Valores faltantes por columna")
st.write(df.isnull().sum())

# Estadísticas
desc = st.checkbox("Mostrar estadísticas descriptivas")
if desc:
    st.subheader("📊 Estadísticas descriptivas")
    st.write(df.describe())

# Gráfico: Precio de venta
st.subheader("💰 Distribución de precios de venta")
fig1, ax1 = plt.subplots()
df["PRECIO DE VENTA"].dropna().hist(bins=15, color="skyblue", edgecolor="black", ax=ax1)
plt.xlabel("Precio de Venta (S/.)")
plt.ylabel("Frecuencia")
st.pyplot(fig1)

# Gráfico: Total de pedidos por categoría
st.subheader("📦 Pedidos por categoría")
cat_count = df["CATEGORÍA"].value_counts()
fig2, ax2 = plt.subplots()
cat_count.plot(kind="bar", ax=ax2, color="orchid", edgecolor="black")
plt.ylabel("Número de pedidos")
st.pyplot(fig2)

# Filtro interactivo
st.subheader("🎨 Filtrar pedidos por color")
color_sel = st.selectbox("Selecciona un color:", df["COLOR"].dropna().unique())
st.write(df[df["COLOR"] == color_sel])

# Gráfico de distribución de TALLAS
st.subheader("📏 Distribución de Tallas")
fig_talla, ax_talla = plt.subplots()
df["TALLA"].value_counts().plot(kind="bar", ax=ax_talla, color="lightgreen", edgecolor="black")
ax_talla.set_ylabel("Cantidad de pedidos")
ax_talla.set_xlabel("Talla")
st.pyplot(fig_talla)

# Gráfico de distribución de COLORES
st.subheader("🎨 Distribución de Colores")
fig_color, ax_color = plt.subplots()
df["COLOR"].value_counts().plot(kind="bar", ax=ax_color, color="lightblue", edgecolor="black")
ax_color.set_ylabel("Cantidad de pedidos")
ax_color.set_xlabel("Color")
st.pyplot(fig_color)

# Promedio de PRECIO DE VENTA por TALLA
st.subheader("💵 Promedio de Precio de Venta por Talla")
precio_prom = df.groupby("TALLA")["PRECIO DE VENTA"].mean().sort_values()
fig_precio, ax_precio = plt.subplots()
precio_prom.plot(kind="bar", ax=ax_precio, color="salmon", edgecolor="black")
ax_precio.set_ylabel("Precio promedio (S/.)")
ax_precio.set_xlabel("Talla")
st.pyplot(fig_precio)
