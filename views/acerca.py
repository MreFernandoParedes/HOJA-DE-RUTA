import streamlit as st
from components.header import mostrar_header
from components.footer import mostrar_footer

mostrar_header("Acerca del proyecto")

st.markdown("<h2>Acerca del proyecto</h2>", unsafe_allow_html=True)

st.markdown("""
    <p>
        Este aplicativo web es una herramienta educativa desarrollada para el
        <strong>Ministerio de Relaciones Exteriores del Perú</strong>, con el
        propósito de documentar y visualizar el avance de la
        <strong>Hoja de Ruta para la integración de la inteligencia artificial
        en la diplomacia digital</strong>.
    </p>
""", unsafe_allow_html=True)

st.markdown("<h3>Tecnologías utilizadas</h3>", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    st.markdown("**Aplicación web**")
    st.markdown("- Python")
    st.markdown("- Streamlit")

with col2:
    st.markdown("**Despliegue y datos**")
    st.markdown("- Render")
    st.markdown("- JSON / SQLite")

st.markdown("<h3>Estándares de diseño</h3>", unsafe_allow_html=True)

st.markdown("""
    <p>
        La interfaz sigue los lineamientos oficiales de la Guía de Servicios
        Digitales del Estado Peruano (<strong>gob.pe</strong>): tipografía
        Roboto, paleta de colores institucional y estructura de plantilla
        definida por la Secretaría de Gobierno Digital.
    </p>
""", unsafe_allow_html=True)

st.markdown("<h3>Contacto</h3>", unsafe_allow_html=True)

st.markdown("""
    <p style='color:#555869;'>
        Ministerio de Relaciones Exteriores del Perú<br>
        Jr. Lampa 545, Lima · <a href='https://www.rree.gob.pe' target='_blank'>www.rree.gob.pe</a>
    </p>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)
mostrar_footer()
