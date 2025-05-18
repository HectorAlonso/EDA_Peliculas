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