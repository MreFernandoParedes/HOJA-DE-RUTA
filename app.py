import streamlit as st
from components.header import cargar_css

st.set_page_config(
    page_title="IA · MRE",
    page_icon="assets/logo_mre.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

cargar_css()

pages = [
    st.Page("views/inicio.py",       title="Inicio",       default=True),
    st.Page("views/introduccion.py", title="Introducción"),
    st.Page("views/entregables.py",  title="Entregables"),
    st.Page("views/acerca.py",       title="Acerca"),
]

pg = st.navigation(pages, position="hidden")

with st.sidebar:
    #st.page_link(pages[0], label="Inicio")
    st.page_link(pages[1], label="Introducción")
    st.page_link(pages[0], label="Entregables")
    st.page_link(pages[3], label="Acerca")

pg.run()
