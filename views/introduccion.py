import streamlit as st
from components.header import mostrar_header
from components.footer import mostrar_footer
from utils.db import get_proyecto

mostrar_header("Introducción")

proyecto = get_proyecto()
st.markdown(
    f"<h1 style='color:#1363D0;'>{proyecto['titulo']}</h1>",
    unsafe_allow_html=True,
)
#st.markdown("<br>", unsafe_allow_html=True)

st.markdown(
    f"<p style='color:#555869;'>{proyecto['institucion']} · {proyecto['anio']}</p>",
    unsafe_allow_html=True,
)    

st.markdown("<h3>Antecedentes y justificación</h3>", unsafe_allow_html=True)
st.markdown("""
    <p>El Ministerio de Relaciones Exteriores (MRE) opera en un contexto internacional donde la
    <strong>diplomacia digital</strong> y la <strong>Inteligencia Artificial (IA)</strong> son cada vez más relevantes
    para la política exterior. Sin embargo, la institución aún no cuenta con una hoja de ruta para
    integrar la IA de forma responsable, estratégica y segura. Esta brecha afecta funciones clave
    como el análisis político, la promoción económica, la cooperación internacional, la comunicación
    estratégica y los servicios consulares.</p>

    <p>En respuesta, el proyecto se plantea como una <strong>intervención de planificación estratégica</strong>
    que incorpora un diagnóstico del estado actual, revisión de tendencias y buenas prácticas,
    análisis de herramientas de IA, identificación de oportunidades y riesgos, y evaluación de
    brechas en capacidades, infraestructura, gestión de datos y talento digital.</p>
""", unsafe_allow_html=True)

st.divider()

st.markdown("<h3>Objetivo general</h3>", unsafe_allow_html=True)
st.markdown("""
    <p>Diseñar y desarrollar la hoja de ruta para la integración de la inteligencia artificial (IA)
    en la diplomacia digital del MRE, incorporando:</p>
""", unsafe_allow_html=True)

col_a, col_b = st.columns(2)
with col_a:
    for item in [
        "Análisis estratégico",
        "Casos de uso",
        "Lineamientos de gobernanza",
    ]:
        st.markdown(f"- {item}")
with col_b:
    for item in [
        "Identificación de riesgos",
        "Propuestas de fortalecimiento institucional",
    ]:
        st.markdown(f"- {item}")

st.divider()

st.markdown("<h3>Alcance</h3>", unsafe_allow_html=True)

col_si, col_no = st.columns(2)
with col_si:
    st.markdown("**El proyecto abarca:**")
    for item in [
        "Investigación documental, datos y entrevistas internas",
        "Mapeo de capacidades actuales en IA para la diplomacia digital",
        "Análisis prospectivo de tendencias globales",
        "Revisión de normativa vigente peruana e internacional",
        "Identificación de casos de uso prioritarios",
        "Propuesta de gobernanza, ética y controles",
        "Elaboración de hoja de ruta estratégica 2026–2028",
    ]:
        st.markdown(f"- {item}")

with col_no:
    st.markdown("**No incluye:**")
    for item in [
        "Desarrollo de soluciones de IA",
        "Implementación de sistemas digitales",
        "Adquisición de infraestructura tecnológica",
    ]:
        st.markdown(f"- {item}")

    

st.markdown("<br><br>", unsafe_allow_html=True)
mostrar_footer()
