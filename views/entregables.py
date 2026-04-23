import streamlit as st
from components.header import mostrar_header
from components.footer import mostrar_footer
from components.cards import mostrar_grilla
from utils.db import get_secciones, get_seccion, actualizar_estado

mostrar_header()

if "seccion_seleccionada" in st.session_state:
    st.session_state["current_seccion_id"] = st.session_state.pop("seccion_seleccionada")

if "current_seccion_id" in st.session_state:
    seccion = get_seccion(st.session_state["current_seccion_id"])

    if seccion is None:
        st.error("Entregable no encontrado.")
        st.stop()

    if st.button("← Volver"):
        del st.session_state["current_seccion_id"]
        st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        f"<h3>Entregable {seccion['id']}: {seccion['titulo']}</h3>",
        unsafe_allow_html=True,
    )

    ESTADOS = ["pendiente", "en_progreso", "completado"]
    nuevo_estado = st.radio(
        "Estado:",
        ESTADOS,
        index=ESTADOS.index(seccion["estado"]),
        horizontal=True,
    )
    if nuevo_estado != seccion["estado"]:
        actualizar_estado(seccion["id"], nuevo_estado)
        st.success(f"Estado actualizado a: {nuevo_estado}")
        st.rerun()

    if seccion["contenido"]:
        for bloque in seccion["contenido"]:
            st.markdown(bloque)
    elif not seccion.get("enlaces"):
        st.info("Este entregable aún no tiene contenido. Se irá completando progresivamente.")

    enlaces = seccion.get("enlaces", [])
    if enlaces:
        st.markdown("<h4>Referencias y enlaces</h4>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        for i, enlace in enumerate(enlaces):
            with col1 if i % 2 == 0 else col2:
                with st.container(border=True):
                    st.markdown(
                        f"<span style='background:#EEF3FB; color:#1363D0; padding:2px 8px; "
                        f"border-radius:10px; font-size:12px;'>{enlace['categoria']}</span>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"**{enlace['nombre']}**")
                    st.markdown(
                        f"<p style='font-size:14px; color:#555869;'>{enlace['descripcion']}</p>",
                        unsafe_allow_html=True,
                    )
                    st.markdown(f"[Ver sitio web →]({enlace['url']})")

else:
    st.markdown("<h3>Entregables del proyecto</h3>", unsafe_allow_html=True)
    mostrar_grilla(get_secciones())

st.markdown("<br><br>", unsafe_allow_html=True)
mostrar_footer()
