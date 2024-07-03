# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 10:17:05 2024

@author: jperezr
"""

import streamlit as st

# Set the title
st.title("CONSAR ESTADÍSTICAS")

# CSS to inject custom styles
st.markdown("""
    <style>
    .stButton > button {
        color: white;
        background-color: #007BFF; /* Blue color */
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
        font-size: 16px;
    }
    .stButton > button:hover {
        background-color: #0056b3; /* Darker blue on hover */
    }
    </style>
    """, unsafe_allow_html=True)

# Create two buttons that link to Google
if st.button('Ir a Cuenatas Administradas por las AFORE'):
    st.write('[Cuentas Administradas por las AFORE](https://consar-cuentas-appistradas-por-las-afore-hlhymabth4creod7bafth.streamlit.app/)')

if st.button('Ir a Traspasos'):
    st.write('[Traspasos](https://consar-traspasos-gdkncxjm8amqr5vr2yyamd.streamlit.app/)')

# Add a section in the sidebar
st.sidebar.title("Ayuda")
st.sidebar.info("""
En esta aplicación puedes encontrar estadísticas de CONSAR. Utiliza los botones para acceder para más información.
""")


# Aviso de derechos de autor
st.sidebar.markdown("""
    ---
    © 2024. Todos los derechos reservados.
    Creado por jahoperi.
""")
