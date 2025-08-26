import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

df_car = pd.read_csv('./notebooks/vehicles_us.csv')

st.header("Anuncios de venta de vehiculos")
build_histogram = st.checkbox('Construir histograma')

if build_histogram:
    st.write('Histograma de kilometraje (odometer)')
    fig = px.histogram(df_car,
                       x= 'odometer',
                       title= 'Distribucion de kilometraje',
                       range_x=[0, 300000]
                       )
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir gráfico de dispersión')

if build_scatter:
    st.write('Dispersion entre kilometraje y precio')
    fig = px.scatter(df_car,
                     x= 'odometer',
                     y= 'price',
                     title= 'Relación kilometro vs precio',
                     hover_data= ['model', 'model_year'],
                     range_x=[0, 400000],
                     range_y=[0, 80000]
                     )
    st.plotly_chart(fig, use_container_width=True)