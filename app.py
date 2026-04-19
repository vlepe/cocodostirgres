import streamlit as st
from urllib.parse import quote

st.set_page_config(page_title="Coco App", layout="centered")

# =========================
# ESTILOS
# =========================
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
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.good {background:#2e7d32;color:white;}
.mid {background:#f39c12;color:white;}
.bad {background:#c0392b;color:white;}

.card {
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 12px;
}

.white {background:#dfe8e1;color:#1f4d2b;}
.gold {background:#e7d7bd;color:#7a4b12;}

.status-good {
    background:#2e7d32;
    color:white;
    padding:12px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
}

.status-mid {
    background:#f39c12;
    color:white;
    padding:12px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
}

.status-bad {
    background:#c0392b;
    color:white;
    padding:12px;
    border-radius:12px;
    text-align:center;
    font-weight:700;
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
</style>
""", unsafe_allow_html=True)

# =========================
# LOGICA
# =========================
def evaluar(precio, tipo):
    kg = 10
    costo_kg = precio / kg

    if tipo == "blanco":
        if costo_kg <= 63:
            return costo_kg, "🔥 Buen negocio", "good"
        elif costo_kg <= 69:
            return costo_kg, "⚠️ Negociar", "mid"
        else:
            return costo_kg, "❌ No conviene", "bad"

    if tipo == "dorado":
        if costo_kg <= 70:
            return costo_kg, "🔥 Buen negocio (mayor tolerancia)", "good"
        elif costo_kg <= 76:
            return costo_kg, "⚠️ Negociar", "mid"
        else:
            return costo_kg, "❌ No conviene", "bad"

# =========================
# HEADER
# =========================
st.markdown('<div class="title">🥥 Simulador Coco</div>', unsafe_allow_html=True)

# =========================
# SLIDERS
# =========================
cajas = st.slider("¿Cuántas cajas?", 10, 2000, 40)

precio = st.slider("Precio por caja", 590, 1500, 650)

# =========================
# CALCULO
# =========================
kg_blanco, msg_b, lvl_b = evaluar(precio, "blanco")
kg_dorado, msg_d, lvl_d = evaluar(precio, "dorado")

# mejor opcion
if kg_blanco < kg_dorado:
    header_msg = msg_b
    header_lvl = lvl_b
    mejor = "Coco Blanco"
    mejor_valor = kg_blanco
else:
    header_msg = msg_d
    header_lvl = lvl_d
    mejor = "Coco Dorado"
    mejor_valor = kg_dorado

# =========================
# BANNER PRINCIPAL
# =========================
st.markdown(f"""
<div class="banner {header_lvl}">
{header_msg}<br>
<small>Mejor opción: {mejor} | ${mejor_valor:.1f}/kg</small>
</div>
""", unsafe_allow_html=True)

# =========================
# TARJETAS
# =========================
col1, col2 = st.columns(2)

with col1:
    st.markdown(f"""
    <div class="card white">
        🥥 Coco Blanco<br><br>
        Cajas: {cajas}<br>
        $/kg: {kg_blanco:.1f}
    </div>
    <div class="status-{lvl_b}">
        {msg_b}
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div class="card gold">
        🥥 Coco Dorado<br><br>
        Cajas: {cajas}<br>
        $/kg: {kg_dorado:.1f}
    </div>
    <div class="status-{lvl_d}">
        {msg_d}
    </div>
    """, unsafe_allow_html=True)

# =========================
# WHATSAPP
# =========================
mensaje = f"""
Simulación coco

Cajas: {cajas}
Precio: ${precio}

Blanco: ${kg_blanco:.1f}/kg → {msg_b}
Dorado: ${kg_dorado:.1f}/kg → {msg_d}

Mejor opción: {mejor}
"""

url = f"https://wa.me/?text={quote(mensaje)}"

st.markdown(f"""
<div class="whatsapp">
<a href="{url}" target="_blank">📲 Abrir mensaje en WhatsApp</a>
</div>
""", unsafe_allow_html=True)
