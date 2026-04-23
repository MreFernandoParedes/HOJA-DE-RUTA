import streamlit as st


def mostrar_footer():
    st.markdown("""
        <div class='footer'>
            <p style='margin:0; font-weight:700;'>
                Ministerio de Relaciones Exteriores del Perú
            </p>
            <p style='margin:4px 0 0 0; color:#DEE3EA;'>
                Hoja de Ruta para la integración de la inteligencia artificial
                en la diplomacia digital · 2026
            </p>
        </div>
    """, unsafe_allow_html=True)
