import streamlit as st
from urllib.parse import quote

st.set_page_config(
    page_title="Simulador de Negociación Coco",
    page_icon="🥥",
    layout="centered"
)

# =========================
# ESTILOS
# =========================
st.markdown("""
<style>
html, body, [class*="css"]  {
    font-family: Arial, sans-serif;
}

.block-container {
    max-width: 780px;
    padding-top: 1.2rem;
    padding-bottom: 2rem;
}

.main-title {
    font-size: 2rem;
    font-weight: 700;
    margin-bottom: 0.3rem;
}

.sub-title {
    color: #666;
    font-size: 0.95rem;
    margin-bottom: 1rem;
}

.banner-good {
    background: #eef8ef;
    border: 3px solid #1d5f2f;
    color: #1d5f2f;
    border-radius: 16px;
    padding: 18px 20px;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.banner-mid {
    background: #fff8e8;
    border: 3px solid #b7791f;
    color: #8a5a12;
    border-radius: 16px;
    padding: 18px 20px;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.banner-bad {
    background: #fff0f0;
    border: 3px solid #a12828;
    color: #8f1d1d;
    border-radius: 16px;
    padding: 18px 20px;
    text-align: center;
    font-size: 1.5rem;
    font-weight: 700;
    margin-bottom: 1rem;
}

.card {
    border-radius: 18px;
    padding: 0;
    overflow: hidden;
    margin-bottom: 1rem;
    border: 1px solid #ddd;
    box-shadow: 0 2px 10px rgba(0,0,0,0.05);
}

.card-header-white {
    background: #e7f1e8;
    color: #225c31;
    padding: 14px 18px;
    font-size: 1.6rem;
    font-weight: 700;
}

.card-header-gold {
    background: #f7ebd9;
    color: #7a4310;
    padding: 14px 18px;
    font-size: 1.6rem;
    font-weight: 700;
}

.metric-box {
    background: #f7f7f7;
    border: 1px solid #ddd;
    border-radius: 14px;
    padding: 12px 16px;
    margin-bottom: 10px;
}

.metric-label {
    font-size: 1rem;
    color: #444;
    margin-bottom: 4px;
}

.metric-value {
    font-size: 2rem;
    font-weight: 700;
    text-align: right;
}

.status-good {
    background: linear-gradient(90deg, #2f7a41, #3f9153);
    color: white;
    padding: 16px;
    border-radius: 14px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    margin-top: 10px;
}

.status-mid {
    background: linear-gradient(90deg, #d68910, #f39c12);
    color: white;
    padding: 16px;
    border-radius: 14px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    margin-top: 10px;
}

.status-bad {
    background: linear-gradient(90deg, #b83232, #d64545);
    color: white;
    padding: 16px;
    border-radius: 14px;
    text-align: center;
    font-size: 1.3rem;
    font-weight: 700;
    margin-top: 10px;
}

.whatsapp-btn a {
    display: block;
    text-align: center;
    text-decoration: none;
    background: linear-gradient(90deg, #228be6, #339af0);
    color: white !important;
    padding: 18px;
    border-radius: 16px;
    font-size: 1.3rem;
    font-weight: 700;
    margin-top: 18px;
    margin-bottom: 10px;
}

.note {
    font-size: 0.9rem;
    color: #666;
    margin-top: 8px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# =========================
# FUNCIONES
# =========================
def evaluar(precio_caja: float, flete_caja: float, kg_por_caja: float, tipo: str):
    costo_total_caja = precio_caja + flete_caja
    costo_kg = costo_total_caja / kg_por_caja

    if tipo == "blanco":
        if costo_kg <= 63:
            return costo_total_caja, costo_kg, "🔥 Buen negocio, vamos!", "good"
        elif costo_kg <= 69:
            return costo_total_caja, costo_kg, "⚠️ Hay que negociar", "mid"
        else:
            return costo_total_caja, costo_kg, "❌ No conviene", "bad"

    if tipo == "dorado":
        if costo_kg <= 70:
            return costo_total_caja, costo_kg, "🔥 Buen negocio (mayor tolerancia)", "good"
        elif costo_kg <= 76:
            return costo_total_caja, costo_kg, "⚠️ Hay que negociar", "mid"
        else:
            return costo_total_caja, costo_kg, "❌ No conviene", "bad"


def clase_status(nivel: str):
    return {
        "good": "status-good",
        "mid": "status-mid",
        "bad": "status-bad"
    }[nivel]


def clase_banner(nivel: str):
    return {
        "good": "banner-good",
        "mid": "banner-mid",
        "bad": "banner-bad"
    }[nivel]


# =========================
# ENCABEZADO
# =========================
st.markdown('<div class="main-title">🥥 Simulador de Negociación Coco</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Comparador rápido para coco rayado blanco y dorado</div>', unsafe_allow_html=True)

# =========================
# INPUT GENERAL
# =========================
st.markdown("### ¿Cuántas cajas?")
cajas = st.slider("Selecciona cajas", min_value=20, max_value=100, value=60, step=10, label_visibility="collapsed")

kg_por_caja = 10.0

col1, col2 = st.columns(2, gap="large")

# =========================
# COCO BLANCO
# =========================
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header-white">🥥 Coco Blanco</div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:16px;">', unsafe_allow_html=True)

    precio_blanco = st.number_input(
        "Precio por caja blanco",
        min_value=0.0,
        value=580.0,
        step=10.0,
        key="precio_blanco"
    )
    flete_blanco = st.number_input(
        "Flete por caja blanco",
        min_value=0.0,
        value=50.0,
        step=10.0,
        key="flete_blanco"
    )

    costo_caja_b, costo_kg_b, mensaje_b, nivel_b = evaluar(precio_blanco, flete_blanco, kg_por_caja, "blanco")

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Cajas</div>
        <div class="metric-value">{cajas}</div>
    </div>
    <div class="metric-box">
        <div class="metric-label">Costo por caja</div>
        <div class="metric-value">${costo_caja_b:,.0f}</div>
    </div>
    <div class="metric-box">
        <div class="metric-label">Costo por kg</div>
        <div class="metric-value">${costo_kg_b:,.1f}</div>
    </div>
    <div class="{clase_status(nivel_b)}">{mensaje_b}</div>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

# =========================
# COCO DORADO
# =========================
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="card-header-gold">🥥 Coco Dorado</div>', unsafe_allow_html=True)
    st.markdown('<div style="padding:16px;">', unsafe_allow_html=True)

    precio_dorado = st.number_input(
        "Precio por caja dorado",
        min_value=0.0,
        value=650.0,
        step=10.0,
        key="precio_dorado"
    )
    flete_dorado = st.number_input(
        "Flete por caja dorado",
        min_value=0.0,
        value=50.0,
        step=10.0,
        key="flete_dorado"
    )

    costo_caja_d, costo_kg_d, mensaje_d, nivel_d = evaluar(precio_dorado, flete_dorado, kg_por_caja, "dorado")

    st.markdown(f"""
    <div class="metric-box">
        <div class="metric-label">Cajas</div>
        <div class="metric-value">{cajas}</div>
    </div>
    <div class="metric-box">
        <div class="metric-label">Costo por caja</div>
        <div class="metric-value">${costo_caja_d:,.0f}</div>
    </div>
    <div class="metric-box">
        <div class="metric-label">Costo por kg</div>
        <div class="metric-value">${costo_kg_d:,.1f}</div>
    </div>
    <div class="{clase_status(nivel_d)}">{mensaje_d}</div>
    """, unsafe_allow_html=True)

    st.markdown("</div></div>", unsafe_allow_html=True)

# =========================
# RESUMEN GENERAL
# =========================
if costo_kg_b < costo_kg_d:
    mejor_tipo = "Coco Blanco"
    mejor_costo = costo_kg_b
    mejor_mensaje = mensaje_b
    mejor_nivel = nivel_b
elif costo_kg_d < costo_kg_b:
    mejor_tipo = "Coco Dorado"
    mejor_costo = costo_kg_d
    mejor_mensaje = mensaje_d
    mejor_nivel = nivel_d
else:
    mejor_tipo = "Ambos iguales"
    mejor_costo = costo_kg_b
    mejor_mensaje = "⚖️ Ambos escenarios dan el mismo costo"
    mejor_nivel = "mid"

st.markdown(
    f'<div class="{clase_banner(mejor_nivel)}">{mejor_mensaje}<br><span style="font-size:1rem;">Mejor opción actual: {mejor_tipo} | ${mejor_costo:,.1f}/kg</span></div>',
    unsafe_allow_html=True
)

# =========================
# MENSAJE WHATSAPP
# =========================
mensaje_whatsapp = f"""Simulación de negociación coco

Cajas: {cajas}

COCO BLANCO
- Precio por caja: ${precio_blanco:,.0f}
- Flete por caja: ${flete_blanco:,.0f}
- Costo total por caja: ${costo_caja_b:,.0f}
- Costo por kg: ${costo_kg_b:,.1f}
- Evaluación: {mensaje_b}

COCO DORADO
- Precio por caja: ${precio_dorado:,.0f}
- Flete por caja: ${flete_dorado:,.0f}
- Costo total por caja: ${costo_caja_d:,.0f}
- Costo por kg: ${costo_kg_d:,.1f}
- Evaluación: {mensaje_d}

Mejor opción: {mejor_tipo} a ${mejor_costo:,.1f}/kg
"""

wa_url = f"https://wa.me/?text={quote(mensaje_whatsapp)}"

st.markdown(
    f'<div class="whatsapp-btn"><a href="{wa_url}" target="_blank">📲 Abrir mensaje en WhatsApp</a></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="note">Si quieres, el siguiente paso es agregar volumen, margen y precio objetivo de reventa.</div>',
    unsafe_allow_html=True
)
