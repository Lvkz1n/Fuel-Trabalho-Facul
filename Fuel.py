# pip install pandas numpy matplotlib seaborn plotly scikit-learn dash

print('hello world')

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 

# Ler o arquivo CSV com a opção low_memory=False
fuel = pd.read_csv("FUEL.csv", low_memory=False)
print(fuel.head())
print(fuel.tail())

# Verifique os valores ausentes
missing_values = fuel.isnull().sum()
print(missing_values)

# Criação de DataFrame de exemplo
df = pd.DataFrame({
    'ID do Veículo': [1, 2, 3],
    'Ano': [4, 5, None],
    'Fabricante': [6, None, 8]
})

print("Antes de descartar colunas com valores NaN:")
print(df)

# Remover colunas com valores NaN
df = df.dropna(axis=1)

print("Depois de eliminar colunas com valores NaN:")
print(df)

# Remover colunas com valores NaN do DataFrame 'fuel'
fuel.drop(columns=['tipo_de_transmissão', 'consumo_cidade_mpg_arredondado_ft2', 'tração', 'supercharger', 'combustível_2'], inplace=True)
print(fuel.shape)
print(fuel.info())

# Distribuição de veículos por ano
plt.figure(figsize=(12, 6))
sns.countplot(x='ano', data=fuel, palette='viridis')
plt.xticks(rotation=90)
plt.title('Distribuição de Veículos por Ano')
plt.xlabel('Ano')
plt.ylabel('Número de Veículos')
plt.tight_layout()
plt.show()

# Distribuição de veículos (Top 20)
plt.figure(figsize=(12, 6))
top_makes = fuel['fabricante'].value_counts().nlargest(20)
sns.barplot(x=top_makes.index, y=top_makes.values, palette='viridis')
plt.xticks(rotation=90)
plt.title('As 20 Principais Marcas de Veículos')
plt.xlabel('Fabricante')
plt.ylabel('Número de Veículos')
plt.tight_layout()
plt.show()

# Distribuição dos tipos de combustível
plt.figure(figsize=(12, 6))
sns.countplot(x='tipo_de_combustível', data=fuel, palette='viridis')
plt.xticks(rotation=45)
plt.title('Distribuição de Tipos de Combustível')
plt.xlabel('Tipo de Combustível')
plt.ylabel('Número de Veículos')
plt.tight_layout()
plt.show()

# Distribuição de cilindros de motor
plt.figure(figsize=(12, 6))
sns.countplot(x='cilindros_do_motor', data=fuel, order=fuel['cilindros_do_motor'].value_counts().index, palette='viridis')
plt.xticks(rotation=45)
plt.title('Distribuição de Cilindros de Motor')
plt.xlabel('Cilindros do Motor')
plt.ylabel('Número de Veículos')
plt.tight_layout()
plt.show()

# Distribuição de veículos por classe
plt.figure(figsize=(12, 6))
vehicle_classes = fuel['classe'].value_counts()
sns.barplot(x=vehicle_classes.index, y=vehicle_classes.values, palette='viridis')
plt.xticks(rotation=90)
plt.title('Distribuição de Veículos por Classe')
plt.xlabel('Classe')
plt.ylabel('Número de Veículos')
plt.tight_layout()
plt.show()
