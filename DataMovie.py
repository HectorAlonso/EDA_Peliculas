import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
import ast



# ! 1- Carga y Limpieza Inicial -----------------------------------------------

# ? Carga del archivo csv. -------------------------------------------------

data = pd.read_csv("Movie_Data_file.csv")

# ? Revisa columnas nulas --------------------------------------------------

print(data.isna().sum())

# ? Convierte Release_year y Runtime a tipo numérico si es necesario. ------

data["Release_year"] = data["Release_year"].fillna(0)
data["Release_year"] = data["Release_year"].astype(int)
data["Runtime"] = data["Runtime"].fillna(0)
data["Runtime"] = data["Runtime"].astype(int)
registros10 = data.head(10)
print(registros10[["Film_title","Release_year","Runtime"]])

# ? Si alguna columna como Genres, Countries o Cast viene ------------------
# ? como string de lista, intenta convertirla a lista real 

print(f"El tipo de datos de Genres es: {type(data['Genres'][0])}")
print(f"El tipo de datos de Countries es: {type(data['Countries'][0])}")
print(f"El tipo de datos de Cast es: {type(data['Cast'][0])}")

registros = data.shape

generosnulos = data[data['Genres'].isna()] 
data = data.drop(generosnulos.index)

Countriesnuloss = data[data['Countries'].isna()]
data = data.drop(Countriesnuloss.index)

Castnulos = data[data['Cast'].isna()]
data = data.drop(Castnulos.index)

registroseliminados = generosnulos.shape[0] + Countriesnuloss.shape[0] + Castnulos.shape[0]

print(f"\nEl numero total de registros es: {registros[0]} - {registroseliminados} = {registros[0]-registroseliminados}")

data["Genres"] = data["Genres"].apply(ast.literal_eval)
data["Countries"] = data["Countries"].apply(ast.literal_eval)
data["Cast"] = data["Cast"].apply(ast.literal_eval)

print(f"\nEl tipo de datos de Genres es: {type(data['Genres'][0])}")
print(f"El tipo de datos de Countries es: {type(data['Countries'][0])}")
print(f"El tipo de datos de Cast es: {type(data['Cast'][0])}")

# ! 2- Exploración general -------------------------------------------------

# ? ¿Cuál es la calificación promedio general de las películas? ---------

promedio_general = data["Average_rating"].mean()
print(f"La calificacion promedio general de las peliculas es: {promedio_general.round(2)}")

# ? ¿Qué porcentaje tiene más de 100,000 ratings? -----------------------

row_con_mas_rating = data[data["Total_ratings"] >= 100000]
row_con_mas_rating = row_con_mas_rating.shape[0]


totalregistros = data.shape[0]
porcentaje = (row_con_mas_rating / totalregistros) * 100
# print(f"El tipo de dato de proncentaje es: {type(porcentaje)}")
porcentaje = round(porcentaje,2)

print(f"Total de Registros: {totalregistros}")
print(f"El numero de registros con mas de 100,000 de rating es: {row_con_mas_rating}")
print(f"El porcentaje con mas de 100,000 de rating es: {porcentaje}%")

# ? ¿Cuáles son los directores más frecuentes? ---------------------------

DirectoresFrecuntes = data["Director"].value_counts()

print("Los directores mas frecuentes son: \n")
print(DirectoresFrecuntes)

# ? ¿Qué películas tienen calificación promedio más alta y más baja? ----

calif_Mas_Alta = data["Average_rating"].max()
calif_Mas_Baja = data["Average_rating"].min()
pelicula_Calif_Mas_Alta = data[data["Average_rating"] == calif_Mas_Alta]
pelicula_Calif_Mas_Baja = data[data["Average_rating"] == calif_Mas_Baja]

print(f"La pelicula con la calificacion mas Alta es: ")
print(pelicula_Calif_Mas_Alta[["Film_title","Average_rating"]])
print(f"\nLa pelicula con la calificacion mas Baja es: ")
print(pelicula_Calif_Mas_Baja[["Film_title","Average_rating"]])

# ! 3- Visualizaciones con interpretación ----------------------------------

# ? a) Histograma de duración 

sns.histplot(data=data["Runtime"])
plt.xlabel("Duracion en Minutos")
plt.ylabel("Cantidad de peliculas")
plt.show()

# ? Boxplot de calificación promedio por idioma original -------------------

data["Original_language"].fillna("Desconocido",inplace=True)

plt.figure(figsize=(28,8))
sns.boxplot(x='Original_language', y='Average_rating', data=data)
plt.grid( color='green', linestyle='--', alpha=0.5)
plt.title('Distribucion de calificacion promedio por idioma')
plt.xticks(rotation=80)
plt.show()

# ? Gráfico de barras de géneros más comunes ------------------------------

Cantidad_Por_Genero = Counter([genero for sublist in data["Genres"] for genero in sublist])

generos = pd.Series(Cantidad_Por_Genero)
generosMasComunes = generos[generos.values >= 200]

generosMasComunes.plot(kind='bar', figsize=(14,10))

for i, valor in enumerate(generosMasComunes):
    plt.text(i, valor + 1, str(valor), ha='center')

plt.title('Géneros más comunes')
plt.xlabel('Generos')
plt.ylabel('Número de Ocurrencias')
plt.grid(axis='y', color='gray', linestyle='--', alpha=0.5)
plt.tight_layout()
plt.xticks(rotation=80) 
plt.show()

# ? Scatterplot: duración vs calificación promedio ------------------------

data["Average_rating"].fillna(round(data["Average_rating"].mean(),2), inplace=True)

x=data['Runtime']
y=data['Average_rating']

plt.scatter(x,y)

plt.title('Relacion entre Calificacion Promedio y Duracion de peliculas')
plt.xlabel('Duracion en Minutos')
plt.ylabel('Promedio Calificacion')
plt.grid(color='green', linestyle='--', alpha=0.3)
plt.show()