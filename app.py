import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="Coco App", layout="centered")

st.markdown("""
<style>
body {
    background-color: #0b1220;
}
.block-container {
    max-width: 800px;
    padding-top: 1rem;
}
.title {
    font-size: 2rem;
    font-weight: 700;
    color: white;
    margin-bottom: 0.5rem;
}
.banner {
    border-radius: 16px;
    padding: 20px;
    text-align: center;
    font-size: 1.25rem;
    font-weight: 700;
    margin-bottom: 1rem;
    line-height: 1.35;
}
.good {background:#2e7d32;color:white;}
.mid {background:#f39c12;color:white;}
.bad {background:#c0392b;color:white;}
.red {background:#b71c1c;color:white;}

.card {
    border-radius: 14px;
    padding: 18px;
    margin-bottom: 12px;
    min-height: 150px;
}
.white {background:#dfe8e1;color:#1f4d2b;}
.gold {background:#e7d7bd;color:#7a4b12;}

.status-good {
    background:#2e7d32;
    color:white;
    padding:14px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
    margin-top: 8px;
}
.status-mid {
    background:#f39c12;
    color:white;
    padding:14px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
    margin-top: 8px;
}
.status-bad {
    background:#c0392b;
    color:white;
    padding:14px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
    margin-top: 8px;
}
.status-red {
    background:#b71c1c;
    color:white;
    padding:14px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
    margin-top: 8px;
}

.card-title {
    font-size: 1.05rem;
    font-weight: 700;
    margin-bottom: 12px;
}
.card-data {
    font-size: 1rem;
    line-height: 1.8;
}

.whatsapp a {
    display:block;
    text-align:center;
    background:#3498db;
    color:white !important;
    padding:16px;
    border-radius:14px;
    text-decoration:none;
    font-weight:700;
    margin-top:12px;
}
small {
    font-size: 0.9rem;
    opacity: 0.95;
}
</style>
""", unsafe_allow_html=True)


def evaluar_blanco(volumen, precio):
    # volumen = F2, precio = G2
    if volumen < 20 or precio <= 580:
        if volumen < 20 and precio <= 580:
            mensaje = "❌ NO se puede cerrar negociación (volumen <20 Y precio ≤$580)"
        elif volumen < 20:
            mensaje = "❌ NO se puede cerrar negociación (volumen menor a 20 cajas)"
        else:
            mensaje = "❌ NO se puede cerrar negociación (precio ≤$580)"
        nivel = "bad"
    elif volumen >= 76 and precio >= 500:
        mensaje = "🟢 Cerrar con compromiso mensual"
        nivel = "good"
    elif volumen >= 76 and precio >= 460 and precio < 500:
        mensaje = "⚠️ Mantener firme, pedir algo a cambio"
        nivel = "mid"
    elif volumen >= 76 and precio < 460:
        mensaje = "🔴 Pedir anticipo o contrato para justificar"
        nivel = "red"
    elif volumen >= 56 and volumen < 76:
        mensaje = "✅ Ceder parcialmente con condición de volumen"
        nivel = "good"
    elif volumen >= 26 and volumen < 56:
        mensaje = "✅ Cerrar rápido, ofrecer continuidad"
        nivel = "good"
    elif volumen < 26:
        mensaje = "⚠️ Mantener precio, no negociar fuerte"
        nivel = "mid"
    else:
        mensaje = "Revisar datos"
        nivel = "mid"

    return mensaje, nivel


def evaluar_dorado(volumen, precio):
    # volumen = F3, precio = G3
    if volumen < 20 or precio <= 610:
        if volumen < 20 and precio <= 610:
            mensaje = "❌ NO se puede cerrar negociación (volumen <20 Y precio ≤$610)"
        elif volumen < 20:
            mensaje = "❌ NO se puede cerrar negociación (volumen menor a 20 cajas)"
        else:
            mensaje = "❌ NO se puede cerrar negociación (precio ≤$610)"
        nivel = "bad"
    elif volumen >= 76 and precio >= 500:
        mensaje = "🟢 Cerrar con compromiso mensual"
        nivel = "good"
    elif volumen >= 76 and precio >= 460 and precio < 500:
        mensaje = "⚠️ Mantener firme, pedir algo a cambio"
        nivel = "mid"
    elif volumen >= 76 and precio < 460:
        mensaje = "🔴 Pedir anticipo o contrato para justificar"
        nivel = "red"
    elif volumen >= 56 and volumen < 76:
        mensaje = "✅ Ceder parcialmente con condición de volumen"
        nivel = "good"
    elif volumen >= 26 and volumen < 56:
        mensaje = "✅ Cerrar rápido, ofrecer continuidad"
        nivel = "good"
    elif volumen < 26:
        mensaje = "⚠️ Mantener precio, no negociar fuerte"
        nivel = "mid"
    else:
        mensaje = "Revisar datos"
        nivel = "mid"

    return mensaje, nivel


def prioridad(nivel):
    orden = {
        "bad": 1,
        "red": 2,
        "mid": 3,
        "good": 4
    }
    return orden.get(nivel, 0)


st.markdown('<div class="title">🥥 Simulador Coco</div>', unsafe_allow_html=True)

cajas = st.slider("¿Cuántas cajas?", 10, 2000, 40)
precio = st.slider("Precio por caja", 590, 1500, 650)

mensaje_b, nivel_b = evaluar_blanco(cajas, precio)
mensaje_d, nivel_d = evaluar_dorado(cajas, precio)

# Cabecera: muestra el mejor resultado por criterio de prioridad.
if prioridad(nivel_b) >= prioridad(nivel_d):
    header_msg = mensaje_b
    header_lvl = nivel_b
    mejor = "Coco Blanco"
else:
    header_msg = mensaje_d
    header_lvl = nivel_d
    mejor = "Coco Dorado"

st.markdown(f"""
<div class="banner {header_lvl}">
{header_msg}<br>
<small>Mejor opción actual: {mejor}</small>
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card white">
        <div class="card-title">🥥 Coco Blanco</div>
        <div class="card-data">
            Cajas: {cajas}<br>
            Precio por caja: ${precio:,.0f}
        </div>
    </div>
    <div class="status-{nivel_b}">
        {mensaje_b}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card gold">
        <div class="card-title">🥥 Coco Dorado</div>
        <div class="card-data">
            Cajas: {cajas}<br>
            Precio por caja: ${precio:,.0f}
        </div>
    </div>
    <div class="status-{nivel_d}">
        {mensaje_d}
    </div>
    """, unsafe_allow_html=True)

mensaje = f"""
Simulación coco

Cajas: {cajas}
Precio por caja: ${precio:,.0f}

COCO BLANCO:
{mensaje_b}

COCO DORADO:
{mensaje_d}

Mejor opción actual: {mejor}
"""

url = f"https://wa.me/?text={quote(mensaje)}"

st.markdown(f"""
<div class="whatsapp">
<a href="{url}" target="_blank">📲 Abrir mensaje en WhatsApp</a>
</div>
""", unsafe_allow_html=True)
