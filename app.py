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

# Create 3 buttons that link to Google
if st.button('Ir a RECURSOS REGISTRADOS EN LAS AFORE'):
    st.write('[RECURSOS REGISTRADOS EN LAS AFORE](https://consar-recursos-registrados-en-las-afore-elnsgisiblu5ruozlqb3d.streamlit.app/)')

if st.button('Ir a ENTRADA Y SALIDA DE RECURSOS DE LAS AFORES'):
    st.write('[ENTRADA Y SALIDA DE RECURSOS DE LAS AFORES](https://consar-entrada-y-salida-de--recursos-de-las-afores-nrnyavoced2.streamlit.app/)')

if st.button('Ir a CUENTAS ADMINISTRADAS POR LAS AFORE'):
    st.write('[CUENTAS ADMINISTRADAS POR LAS AFORE](https://consar-cuentas-appistradas-por-las-afore-hlhymabth4creod7bafth.streamlit.app/)')

if st.button('Ir a TRASPASOS'):
    st.write('[TRASPASOS](https://consar-traspasos-gdkncxjm8amqr5vr2yyamd.streamlit.app/)')

if st.button('Ir a MONTOS'):
    st.write('[MONTOS](https://consar-montos-nhbjnm56txbnz5rvrmrd7z.streamlit.app/)')

if st.button('Ir a INDICADOR DE RENDIMIENTO NETO (IRN) DE LAS SIEFORES'):
    st.write('[INDICADOR DE RENDIMIENTO NETO (IRN) DE LAS SIEFORES](https://consar-irn-f8qd7noi8arngh2p7pzcgf.streamlit.app/)')

# Add a section in the sidebar
st.sidebar.title("Ayuda")
st.sidebar.info("""
En esta aplicación puedes encontrar estadísticas de CONSAR. Utiliza los botones para acceder para más información.
""")


# Aviso de derechos de autor
#st.sidebar.markdown("""
#    ---
#    © 2024. Todos los derechos reservados.
#    Creado por Javier Horacio Pérez Ricárdez.
#""")

# Pie de página en la barra lateral
st.sidebar.write("© 2024 Todos los derechos reservados")
st.sidebar.write("© 2024 Creado por: Javier Horacio Pérez Ricárdez")
st.sidebar.write("PensionISSSTE: Analista UEAP "B"")
