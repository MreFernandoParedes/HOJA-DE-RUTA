import streamlit as st
from components.header import cargar_css

st.set_page_config(
    page_title="IA · MRE",
    page_icon="assets/logo_mre.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

cargar_css()

pages = [
    st.Page("views/inicio.py",      title="Inicio",       default=True),
    st.Page("views/entregables.py", title="Entregables"),
    st.Page("views/acerca.py",      title="Acerca"),
]

st.session_state["_pages"] = pages

pg = st.navigation(pages, position="hidden")
pg.run()
