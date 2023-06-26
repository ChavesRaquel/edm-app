import streamlit as st
import csv
import pandas as pd
import plotly.express as px
import folium
from streamlit_folium import st_folium
from folium import plugins

add_selectbox = st.sidebar.selectbox('Elige el tipo de transporte',('Turismo','Moto','Bicicleta'))

def abrir_html(filename):
    with open(filename, "r") as file:
        html_content = file.read()
        return html_content
    
if add_selectbox == 'Bicicleta':
    bicis = abrir_html('mapa-bicicletas.html')
    st.components.v1.html(bicis, height=600)
    
elif add_selectbox == 'Moto':
    moto = abrir_html('mapa-motos.html')
    st.components.v1.html(moto, height=600)

elif add_selectbox == 'Turismo':
    coches = abrir_html('mapa-coches.html')
    st.components.v1.html(coches, height=600)