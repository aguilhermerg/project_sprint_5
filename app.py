import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('../data/vehicles.csv')  # lendo os dados

st.header("Criando gráficos sobre dados de automóveis")

# criando caixa de selecao histograma
build_histogram = st.checkbox("Criar histograma")

if build_histogram:  # se a caixa de selecao for selecionada
    # escrever uma mensagem
    st.write(
        "Criando um histograma para o conjunto de dados de anúncios de vendas de carro")

    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

# criando caixa de selecao para grafico de dispersão
build_scatter_plot = st.checkbox("Criar gráfico de dispersão")

if build_scatter_plot:
    st.write(
        "Criando um gráfico de dispersão para o conjunto de dados de anúncios de vendas de carro")

    fig = px.scatter(car_data, x="odometer")

    st.plotly_chart(fig, use_container_width=True)