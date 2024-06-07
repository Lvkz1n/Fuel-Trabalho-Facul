import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página do Streamlit
st.set_page_config(layout="wide")
st.title("Análise de Dados de Carros De Diferentes Épocas e Fabrincantes")

# Carregando os dados
df = pd.read_csv("FUEL.csv")


# Adicionando o CSS customizado
with open("style.css") as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)


# Filtros na barra lateral
st.sidebar.header("Filtros")
anos = st.sidebar.multiselect(
    "Selecione o(s) ano(s):",
    options=df['ano'].unique(),
    default=df['ano'].unique()[:1]
)

top_fabricante = df['fabricante'].value_counts().nlargest(1).index.tolist()
fabricantes = st.sidebar.multiselect(
    "Selecione o(s) fabricante(s):",
    options=df['fabricante'].unique(),
    default=top_fabricante
)

# Filtrando os dados com base nos filtros selecionados
df_filtered = df[(df['ano'].isin(anos)) & (df['fabricante'].isin(fabricantes))]

# Layout da página com colunas
col1, col2 = st.columns(2)
col3, col4, col5 = st.columns(3)

# Gráfico 1: Distribuição de Veículos por Modelo
fig1 = px.bar(df_filtered, x='modelo', title='Distribuição de Veículos por Ano', 
              labels={'modelo': 'Modelos', 'count': 'Versões'})
col1.plotly_chart(fig1, use_container_width=True)

# Gráfico 2: Relação entre Deslocamento do Motor, Consumo na Cidade
fig2 = px.scatter(df_filtered, x='deslocamento_do_motor', y='consumo_cidade_mpg_ft1', color='fabricante', 
                     title='Relação entre Deslocamento do Motor, Consumo de Combustível na Cidade e Pontuação de Eficiência de Combustível',
                     labels={'deslocamento_do_motor': 'Deslocamento do Motor', 'consumo_cidade_mpg_ft1': 'Consumo de Combustível na Cidade (MPG)', 'fabricante': 'Fabricante'})
col2.plotly_chart(fig2, use_container_width=True)

# Gráfico 3: Distribuição de Veículos por Classe e Fabricante
fig3 = px.bar(df_filtered, y='classe', color='fabricante', orientation='h',
              title='Distribuição de Veículos por Classe e Fabricante',
              labels={'classe': 'Classe', 'fabricante': 'Fabricante', 'count': 'Quantidade'})
col3.plotly_chart(fig3, use_container_width=True)

# Gráfico 4: Tipos de Combustível
fig4 = px.pie(df_filtered, names='combustível_1', title='Tipos de Combustível', 
              labels={'combustível_1': 'Combustível'})
col4.plotly_chart(fig4, use_container_width=True)

# Gráfico 5: Distribuição de Veículos por Classe e Turbo/Não Turbo
fig5 = px.bar(df_filtered, x='classe', color='turbo', barmode='stack',
              title='Distribuição de Veículos por Classe e Turbo/Não Turbo no Ano Selecionado',
              labels={'classe': 'Classe', 'turbo': 'Turbo', 'count': 'Quantidade'})
col5.plotly_chart(fig5, use_container_width=True)
