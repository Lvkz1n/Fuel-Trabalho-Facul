import streamlit as st
import pandas as pd
import plotly.express as px


def load_data():
    data = pd.read_csv("FUEL.csv", sep=",", converters={'ano': lambda x: int(x.replace('.', ''))})
    return data


df = load_data()


st.set_page_config(layout="wide")

st.title("Análise de Dados de Combustível")

st.sidebar.header("Filtros")

anos = st.sidebar.multiselect(
    "Selecione o(s) ano(s):",
    options=df['ano'].unique(),
    default=df['ano'].unique()
)


fabricantes = st.sidebar.multiselect(
    "Selecione o(s) fabricante(s):",
    options=df['fabricante'].unique(),
    default=df['fabricante'].unique()
)


df_filtrado = df[(df['ano'].isin(anos)) & (df['fabricante'].isin(fabricantes))]


fig1 = px.histogram(df_filtrado, x='ano', title='Distribuição dos Veículos por Ano')
fig2 = px.scatter(df_filtrado, x='ano', y='consumo_cidade_mpg_ft1', color='fabricante', title='Consumo na Cidade (MPG) por Ano e Fabricante')
fig3 = px.histogram(df_filtrado, x='fabricante', y='consumo_cidade_mpg_ft1', title='Consumo na Cidade (MPG) por Fabricante')
fig4 = px.scatter(df_filtrado, x='ano', y='consumo_estrada_mpg_ft1', color='fabricante', title='Consumo na Estrada (MPG) por Ano e Fabricante')
fig5 = px.histogram(df_filtrado, x='fabricante', y='consumo_combinado_mpg_ft1', title='Consumo Combinado (MPG) por Fabricante')


st.plotly_chart(fig1, use_container_width=True)
st.plotly_chart(fig2, use_container_width=True)
st.plotly_chart(fig3, use_container_width=True)
st.plotly_chart(fig4, use_container_width=True)
st.plotly_chart(fig5, use_container_width=True)
