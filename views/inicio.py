import streamlit as st
from components.header import mostrar_header
from components.footer import mostrar_footer
from components.cards import mostrar_grilla
from utils.db import get_proyecto, get_secciones

mostrar_header("Entregables del proyecto")

proyecto = get_proyecto()
#st.markdown(
#    f"<h1 style='color:#1363D0;'>{proyecto['titulo']}</h1>",
#    unsafe_allow_html=True,
#)
#st.markdown("<br>", unsafe_allow_html=True)

secciones = get_secciones()
mostrar_grilla(secciones)


st.markdown("<br><br>", unsafe_allow_html=True)
mostrar_footer()
