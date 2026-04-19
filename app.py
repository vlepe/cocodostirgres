import streamlit as st

st.title("Simulador de Negociación Coco 🥥")

cajas = st.number_input("Cajas", min_value=1, value=20)
precio = st.number_input("Precio por caja", value=580)
flete = st.number_input("Flete por caja", value=50)
tipo = st.selectbox("Tipo", ["Blanco", "Dorado"])

costo = precio + flete
precio_kg = costo / 10

if precio_kg < 65:
    mensaje = "🔥 Buen negocio"
elif precio_kg < 75:
    mensaje = "⚠️ Negociar"
else:
    mensaje = "❌ No conviene"

if tipo == "Dorado":
    mensaje += " (mayor tolerancia)"

st.subheader("Resultado")
st.write(f"Costo por caja: ${costo}")
st.write(f"Precio por kg: ${precio_kg}")
st.write(f"Recomendación: {mensaje}")
