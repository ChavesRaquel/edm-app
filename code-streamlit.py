import streamlit as st
import csv
import pandas as pd
import plotly.graph_objects as go
import folium
from streamlit_folium import st_folium
from folium import plugins

st.set_page_config(page_title="Encuentra tu aparcamiento en Valencia",
                   layout ="wide",
                   initial_sidebar_state="expanded",
                   page_icon = "🗺️")
                   
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
        go.Bar(name='No Regulados', x=categorias, y=no_regulados, hovertemplate='Nº de plazas no reguladas: %{y}<extra></extra>', marker=dict(color='#E0DB64')),
        go.Bar(name='Parking', x=categorias, y=parking, hovertemplate='Plazas en parkings: %{y}<extra></extra>', marker=dict(color='#6EE2F4')),    
        go.Bar(name='ORA', x = categorias, y=ora, hovertemplate='Plazas en ORA: %{y}<extra></extra>', marker=dict(color='#DE9528')),
        go.Bar(name='Otros', x=categorias, y= otros, hovertemplate='Otros tipos de plazas: %{y}<extra></extra>', marker=dict(color='#A3FF9B'))
    ])

    fig.update_layout(barmode='stack', 
                    title='¿Cuántas plazas hay por barrio?',
                    plot_bgcolor = '#675F5F', 
                    paper_bgcolor = '#675F5F',
                    font=dict(color='#F0F2F6'),
                    yaxis=dict(showgrid=False, zeroline=True, zerolinecolor='#F0F2F6'))

    
    fig.update_xaxes(title='Barrios')
    fig.update_yaxes(title='Nº plazas')
    fig.update_layout(width=1300, height=600)

    container = st.container()
    with container:
        container.markdown(
            f"""
            <style>
            .containerStyle {{
                display: flex;
                justify-content: center;
                align-items: center;
                height: {600}px;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
        container.plotly_chart(fig, use_container_width=True)