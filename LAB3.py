import pandas as pd
import streamlit as st 

#PARTE 1, 20PTS LECTURA Y EXPLORACIÓN INICIAL:
#CVS 1, VEHICULOS ELECTRICOS:
df_vehiculos = pd.read_csv("Electric_Vehicle_Population-2.csv")
st.title("Análisis de los Vehiculos Electricos")
st.write(f"Filas: {df_vehiculos.shape[0]}, Columnas: {df_vehiculos.shape[1]}")
st.write ("COLUMNAS: ", list(df_vehiculos.columns))
st.dataframe(df_vehiculos.head(6))
st.write("Estadísticas generales: ", df_vehiculos.describe())

#CSV 2, GIMNASIO:
df_gimnasio = pd.read_csv("GymExerciseTracking.csv")
st.title ("Análisis del Gimnasio")
st.write(f"Filas: {df_gimnasio.shape[0]}, Columnas: , {df_gimnasio.shape[1]}")
st.write ("COLUMNAS: ", list(df_gimnasio.columns))
st.dataframe(df_gimnasio.head(6))
st.write("Estadísticas generales: ", df_gimnasio.describe())

#CSV 3, VIDEOJUEGOS:
df_videojuegos = pd.read_csv("steam_store_data_2024.csv")
st.title("Análisis de los videojuegos: ")
st.write(f"Filas: , {df_videojuegos.shape[0]}, Columnas: , {df_videojuegos.shape[1]}")
st.write("COUMNAS: ", list(df_videojuegos.columns))
st.dataframe(df_videojuegos.head(6))
st.write("Estadísticas generales: ", df_videojuegos.describe())

#CSV 4, NETFLIX:
df_netflix = pd.read_csv ("netflix_titles.csv")
st.title ("Análisis de NETFLIX")
st.write(f"Filas: {df_netflix.shape[0]}, Columnas: {df_netflix.shape [1]}")
st.write("COLUMNAS: ", list(df_netflix.columns))
st.dataframe(df_netflix.head(6))
st.write("Estadísticas generales: ", df_netflix.describe())

