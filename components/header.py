import streamlit as st
import os
import base64

CSS_RUTA  = os.path.join(os.path.dirname(__file__), "..", "assets", "style.css")
LOGO_RUTA = os.path.join(os.path.dirname(__file__), "..", "assets", "logo_mre.png")


def cargar_css():
    with open(CSS_RUTA, encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


def _logo_base64():
    with open(LOGO_RUTA, "rb") as f:
        return base64.b64encode(f.read()).decode()


def mostrar_header(titulo_pagina=""):
    logo = _logo_base64()
    st.markdown(f"""
        <div style='display:flex; align-items:center; gap:20px; padding:8px 0 4px 0;'>
            <a href='/' target='_self'>
                <img src='data:image/png;base64,{logo}' width='200'
                     style='cursor:pointer; display:block;'>
            </a>
            <h4 style='margin:0; color:#1363D0;'>{titulo_pagina}</h4>
        </div>
    """, unsafe_allow_html=True)
    st.divider()
