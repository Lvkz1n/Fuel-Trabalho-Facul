#pip install. pip install pandas numpy matplotlib seaborn plotly scikit-learn dash

print('hello world')

import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 




fuel = pd.read_csv("FUEL.csv")
print(fuel.head())
print (fuel.tail ())

# Verifique os valores ausentes

missing_values = fuel.isnull().sum()
print (missing_values)

# Assumindo que o DF é o seu quadro de dados
df = pd.DataFrame({
    'A': [1, 2, 3],
    'B': [4, 5, None],
    'C': [6, None, 8]
})

print("Before dropping columns with NaN values:")
print(df)

# Soltar colunas com valores de NaN
df = df.dropna(axis=1)

print("After dropping columns with NaN values:")
print(df)

# Excluindo coluna com valores de NaN

del fuel['transmission_type']
del fuel['range_ft2']
fuel.shape
(38113, 79)
fuel.head()

del fuel['drive']
fuel.info()

del fuel['supercharger']
del fuel['fuel_type_2']
fuel.describe()


# Distribuição de veículos por ano

df = fuel

plt.figure(figsize=(12, 6))
sns.countplot(x='year', data=df, palette='viridis')
plt.xticks(rotation=90)
plt.title('Distribution of Vehicles by Year')
plt.xlabel('Year')
plt.ylabel('Number of Vehicles')
plt.tight_layout()
plt.show()

# Distribuição de veículos (Top 20)

plt.figure(figsize=(12, 6))
top_makes = df['make'].value_counts().nlargest(20)
sns.barplot(x=top_makes.index, y=top_makes.values, palette='viridis')
plt.xticks(rotation=90)
plt.title('Top 20 Vehicle Makes')
plt.xlabel('Make')
plt.ylabel('Number of Vehicles')
plt.tight_layout()
plt.show()

# Distribuição dos tipos de combustível

plt.figure(figsize=(12, 6))
sns.countplot(x='fuel_type', data=df, palette='viridis')
plt.xticks(rotation=45)
plt.title('Distribution of Fuel Types')
plt.xlabel('Fuel Type')
plt.ylabel('Number of Vehicles')
plt.tight_layout()
plt.show()

# Distribuição de cilindros de motor

plt.figure(figsize=(12, 6))
sns.countplot(x='engine_cylinders', data=df, order=df['engine_cylinders'].value_counts().index, palette='viridis')
plt.xticks(rotation=45)
plt.title('Distribution of Engine Cylinders')
plt.xlabel('Engine Cylinders')
plt.ylabel('Number of Vehicles')
plt.tight_layout()
plt.show()


# Distribuição de veículos por classe

plt.figure(figsize=(12, 6))
vehicle_classes = df['class'].value_counts()
sns.barplot(x=vehicle_classes.index, y=vehicle_classes.values, palette='viridis')
plt.xticks(rotation=90)
plt.title('Distribution of Vehicles by Class')
plt.xlabel('Class')
plt.ylabel('Number of Vehicles')
plt.tight_layout()
plt.show()







