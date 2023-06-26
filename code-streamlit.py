import streamlit as st
import csv
import pandas as pd
import plotly.graph_objects as go
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

    datos = pd.read_csv('aparcaments-per-districtes-barris.csv', sep = ';')
    selec = datos.loc[(datos['BARRI'] == 'Districte') & (datos['GRUP'] == 'Grup')]

    categorias = selec['DISTRICTE']
    parking = selec['PÀRQUINGS']
    vados = selec['GUALS']
    no_regulados = selec['LLIURES']
    ora = selec['ORA']
    otros = selec['ALTRES']

    fig = go.Figure(data=[
        go.Bar(name='No Regulados', x=categorias, y=no_regulados, hovertemplate='Nº de plazas no reguladas: %{y}<extra></extra>', marker=dict(color='#6FEDEB')),
        go.Bar(name='Vados', x=categorias, y=vados, hovertemplate='Nº de vados: %{y}<extra></extra>', marker=dict(color='#EDD458')),
        go.Bar(name='Parking', x=categorias, y=parking, hovertemplate='Plazas en parkings: %{y}<extra></extra>', marker=dict(color='#A18D2B')),    
        go.Bar(name='ORA', x = categorias, y=ora, hovertemplate='Plazas en ORA: %{y}<extra></extra>', marker=dict(color='#EDA26F')),
        go.Bar(name='Otros', x=categorias, y= otros, hovertemplate='Otros tipos de plazas: %{y}<extra></extra>', marker=dict(color='#A3FF9B'))
    ])

    fig.update_layout(barmode='stack', 
                    title='¿Cuántas plazas hay por barrio?',
                    plot_bgcolor = '#3C3C3C', 
                    paper_bgcolor = '#3C3C3C',
                    font=dict(color='#F0F2F6'),
                    yaxis=dict(showgrid=False))
    fig.update_xaxes(title='Barrios')
    fig.update_yaxes(title='Nº plazas')

    st.plotly_chart(fig)