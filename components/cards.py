import streamlit as st


def mostrar_tarjeta(seccion):
    CIRCULOS = {
        "pendiente":   "🔴",
        "en_progreso": "🟡",
        "completado":  "🟢",
    }
    circulo = CIRCULOS.get(seccion["estado"], "⚪")
    label = f"{circulo}  Entregable {seccion['id']}\n{seccion['titulo']}"
    if st.button(label, key=f"btn_{seccion['id']}", use_container_width=True):
        st.session_state["seccion_seleccionada"] = seccion["id"]
        st.switch_page("views/entregables.py")


def mostrar_grilla(secciones):
    col1, col2 = st.columns(2)
    for i, seccion in enumerate(secciones):
        with col1 if i % 2 == 0 else col2:
            mostrar_tarjeta(seccion)
