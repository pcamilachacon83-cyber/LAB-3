#Universidad del Valle de Guatemala
#Facultad de Ingeniería
#Algoritmos y Programación Básica
#Paula Camila Chacón Mérida - 26860 y Luis Esteban Ciurla Rivas - 26403
#Laboratorio 3
#03/05/2026

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


#PARTE 2, 8PTS, INGRESO DE NUEVOS DATOS:

#INGRESO DE NUEVOS DATOS PARA CSV 3, VIDEOJUEGOS:
st.header("Ingreso de datos para videojuegos: ")
with st.form ("Nuevos videojuegos"):
    st.write ("Registra un nuevo videojuego: ")
    title_vj = st.text_input("Nombre del Juego: ")
    description_vj = st.text_input("Descripción del juego: ")
    price = st.number_input("Precio del juego: ")
    salepercent = st.slider(",Seleccione el descuento del juego: ", 0,100,0)
    recentReviews = st.text_input("Reseñas recientes del juego: ")
    allReviews = st.text_input ("Reseñas del videojuego: ")
    boton_vj = st.form_submit_button("Añadir Videojuego")
    if boton_vj:
        nueva_fila_vj = {
            "title" : title_vj, 
            "description" : description_vj,
            "rrice" : price,
            "salePercent" : f"-{salepercent}%",
            "recentReviews" : recentReviews,
            "allReviews" : allReviews,
        }
        fila_nueva = pd.DataFrame([nueva_fila_vj])
        df_videojuegos = pd.concat([df_videojuegos, fila_nueva], ignore_index=True)
        st.success("¡Videojuego añadido con éxito!")
     


#INGRESO DE NUEVOS DATOS PARA CSV 4, NETFLIX:
st.header("Ingreso de datos para netflix: ")
with st.form ("Nuevos ingresos para NETFLIX: "):
    st.write ("Registre un nuevo proyecto: ")
    show_id = st.text_input("Id del show: ")
    tipo = st.text_input("Ingrese el tipo del proyecto: ")
    title = st.text_input("Ingrese el título: ")
    director = st.text_input("Ingrese el nombre del director: ")
    cast = st.text_input("Ingrese el nombre de los actores: ")
    country = st.text_input("Ingrese el país de grabación: ")
    date_added = st.text_input("Ingrese la fecha en la que se añadio: ")
    release_year = st.number_input("Ingrese el año en que se estreno: ")
    rating = st.text_input("Ingrese el rango: ")
    duration = st.text_input("Ingrese cuanto dura (minutos/temporadas): ")
    listed_in = st.text_input("Ingrese en que está listado (drama, comedia, romance, etc): ")
    description = st.text_input("Ingrese una la sinopsis: ")
    boton_n = st.form_submit_button("Añadir proyeto")
    if boton_n:
        nueva_fila_n = {
            "show_id": show_id,
            "type": tipo,
            "title": title,
            "director": director,
            "cast": cast,
            "country": country,
            "date_added": date_added,
            "release_year": release_year,
            "rating":  rating,
            "duration": duration,
            "listed_in": listed_in,
            "description": description,
        }
        fila_nueva_n = pd.DataFrame([nueva_fila_n])
        df_netflix = pd.concat([df_netflix, fila_nueva_n], ignore_index=True)
        st.success("¡Proyecto añadido con éxito!")

#PARTE 3, 24 pts, FILTROS

#CSV 1, VEHÍCULOS
st.header("Busqueda de vehículos según los filtros que quiera: ")
año = st.sidebar.number_input("Vehículo del año que desea: ", 2000, 2025, 2000)
precio = st.sidebar.number_input("Ingrese su precio máximo: ",0.0, 845000.0, 845000.0)
df_vehiculos_f = df_vehiculos[(df_vehiculos['Model Year'] < año) & (df_vehiculos['Base_MSRP'] < precio)]
st.dataframe (df_vehiculos_f)

#CSV 2, GIMNASIO:
st.header ("Busqueda de datos según filtros: ")
calorias =st.sidebar.number_input("Calorías quemadas: ",0.0, 100.0, 100.0)
grasa = st.sidebar.slider ("Porcentaje de grasa máxima: ",  0, 100, 5)
df_gimnasio_f = df_gimnasio[(df_gimnasio['Calories_Burned'] >= calorias) & (df_gimnasio['Fat_Percentage'] <= grasa)]
st.dataframe (df_gimnasio_f)

#CSV 3, VIDEOJUEGOS:
st.header("Búsqueda de videojuegos según filtros:")
df_videojuegos['price_num'] = df_videojuegos['price'].replace('[\$,]', '', regex=True)
df_videojuegos['price_num'] = pd.to_numeric(df_videojuegos['price_num'], errors='coerce')
df_videojuegos['salePercent_num'] = df_videojuegos['salePercentage'].str.replace('%', '', regex=False).str.replace('-', '', regex=False)
df_videojuegos['salePercent_num'] = pd.to_numeric(df_videojuegos['salePercent_num'], errors='coerce')
precio_vj = st.sidebar.number_input("Ingrese precio mínimo:", min_value=0.0, value=0.0)
descuento_vj = st.sidebar.slider("Descuento menor al (%):", 0, 100, 55)
df_videojuegos_f = df_videojuegos[
    (df_videojuegos['price_num'] > precio_vj) & 
    (df_videojuegos['salePercent_num'] < descuento_vj)
]
st.dataframe(df_videojuegos_f)

#CSV 4, NETFLIX:
st.header("Búsqueda de proyectos según filtros: ")
df_netflix['duration_num'] = df_netflix['duration'].str.replace(' min', '', regex=False)
df_netflix['duration_num'] = pd.to_numeric(df_netflix['duration_num'], errors='coerce')
df_netflix['year_added_clean'] = pd.to_datetime(df_netflix['date_added'], errors='coerce').dt.year
duracion = st.sidebar.number_input("Películas más largas de (minutos):", min_value=0, value=0)
año_adicion = st.sidebar.number_input("Contenido añadido antes del año:", 2007, 2025, 2020)
df_netflix_f = df_netflix[
    (df_netflix['duration_num'] > duracion) & 
    (df_netflix['year_added_clean'] < año_adicion)
]
st.dataframe(df_netflix_f)

#Parte 4

#CSV 1, VEHICULOS:
st.header ("Nueva categoria de vehículos: ")
def categorizar_rango(r):
    if r < 100:
        return "Bajo"
    elif 100 <= r <= 250:
        return "Medio"
    else:
        return "Alto"
df_vehiculos['RangoCategoria'] = df_vehiculos['Electric_Range'].apply(categorizar_rango)
st.subheader("Conteo por Categoría de Rango")
conteo_v = df_vehiculos['RangoCategoria'].value_counts()
st.bar_chart(conteo_v)
analisis_v = df_vehiculos.groupby('RangoCategoria').agg({
    'Base_MSRP': 'mean',
    'Model Year': 'mean',
    'Electric_Range': 'std'
})
st.table(analisis_v)

#CSV 2, GIMNASIO:
st.header("Nueva categoria de GYM: ")
def categorizar_frecuencia(f):
    if f < 3: 
        return "Baja"
    elif 3 <= f <= 5:
        return "Moderada"
    else:
        return "Alta"
df_gimnasio['NivelFrecuencia'] = df_gimnasio['Workout_Frequency (days/week)'].apply(categorizar_frecuencia)
st.subheader("Registros por Nivel de Frecuencia")
st.bar_chart(df_gimnasio['NivelFrecuencia'].value_counts())
st.write("Métricas por Frecuencia:")
analisis_g = df_gimnasio.groupby('NivelFrecuencia').agg({
    'Session_Duration (hours)': 'mean',
   'Experience_Level': 'mean',
    'BMI': 'std'
})
st.table(analisis_g)

#CSV 3, VIDEOJUEGOS:
st.header ("Nueva categoria para videojuegos: ")
def categorizar_gama(p):
    if p < 10:
        return "Baja"
    elif 10 <= p <= 24:
        return "Media"
    else: 
        return "Alta"
df_videojuegos['GamaJuego'] = df_videojuegos['price_num'].apply(categorizar_gama)
st.subheader("Cantidad de Juegos por Gama")
st.bar_chart(df_videojuegos['GamaJuego'].value_counts())
st.write("Métricas por Gama de Precio:")
analisis_vj = df_videojuegos.groupby('GamaJuego').agg({
    'price_num': ['mean', 'std'],
    'salePercent_num': 'mean'
})
st.table(analisis_vj)

#CSV 4, NETFLIX:
st.header("Nueva categoria para netflix: ")
audiencias = {
    'Niños': ['G', 'TV-Y', 'TV-G', 'TV-Y7', 'TV-Y7-FV'],
    'Adolescentes': ['PG', 'TV-PG'],
    'Adultos Jóvenes': ['PG-13', 'TV-14'],
    'Adultos': ['R', 'TV-MA', 'NC-17']
}
def categorizar_audiencia(a):
    for c, ratings in audiencias.items():
        if a in ratings: return c
    return "Otro"
df_netflix['TipoAudiencia'] = df_netflix['rating'].apply(categorizar_audiencia)
st.subheader("Contenido por Tipo de Audiencia")
st.bar_chart(df_netflix['TipoAudiencia'].value_counts())
st.write("Análisis por Audiencia:")
analisis_n = df_netflix.groupby('TipoAudiencia').agg({
    'type': lambda x: x.mode()[0] if not x.mode().empty else "N/A",
    'duration_num': 'mean'
})
st.table(analisis_n)

#PARTE 5, PREGUNTAS, 12 PTS
st.divider()
st.title("5. Análisis de Preguntas Clave")

#CSV 1, VEHICULOS:
st.header("Vehículos Eléctricos")
resumen_rango_año = df_vehiculos.groupby("Model Year")['Electric_Range'].mean()
st.subheader("¿El rango aumenta con los años?")
st.line_chart(resumen_rango_año)
st.write("Promedio de rango en los últimos 5 años:", resumen_rango_año.tail())
corr_v = df_vehiculos['Base_MSRP'].corr(df_vehiculos['Electric_Range'])
st.subheader("¿A mayor precio, mayor rango?")
st.write(f"Coeficiente de correlación de Pearson: {corr_v:.2f}")

#CSV 2, GIMNASIO
st.header("Gimnasio")
corr_g = df_gimnasio['Calories_Burned'].corr(df_gimnasio["Session_Duration (hours)"])
st.subheader("¿Más tiempo equivale a más calorías?")
st.write(f"Correlación entre duración y calorías: {corr_g:.2f}")
resumen_grasa = df_gimnasio.groupby('Experience_Level')['Fat_Percentage'].mean()
st.subheader("Grasa corporal promedio por Nivel de Experiencia")
st.bar_chart(resumen_grasa)

#CSV 3, VIDEOJUEGOS:
st.header("Videojuegos")
calificacion_gama = df_videojuegos.groupby('GamaJuego')['allReviews'].value_counts().unstack().fillna(0)
st.subheader("Distribución de reseñas por Gama de Juego")
st.dataframe(calificacion_gama)
mejores_calificados = df_videojuegos[df_videojuegos['allReviews'].str.contains('Positive', na=False)]
min_p = mejores_calificados['price_num'].min()
max_p = mejores_calificados['price_num'].max()
st.subheader("Rango de precios de juegos con mejores reseñas")
st.info(f"El rango de precios para juegos 'Positive' va desde ${min_p} hasta ${max_p}")

#CSV 4, NETFLIX:
st.header("Netflix")
Top_10_recientes = df_netflix.sort_values(by='year_added_clean', ascending=False).head(10)
st.subheader("10 títulos más recientes añadidos al catálogo")
st.table(Top_10_recientes[['title', 'date_added']])
paises_top = df_netflix['country'].value_counts().head(10)
st.subheader("Top países con más producciones")
st.bar_chart(paises_top)

#PARTE 6, 4 PTS:
import os
st.divider()
st.subheader("Auditoría de Archivos")
archivos_esperados = [
    "Electric_Vehicle_Population_Actualizado.csv",
    "GymExerciseTracking_Actualizado.csv",
    "steam_store_data_2024_Actualizado.csv",
    "netflix_titles_Actualizado.csv"
]
for archivo in archivos_esperados:
    if os.path.exists(archivo):
        st.write(f"Archivo encontrado en carpeta: `{archivo}`")
    else:
        st.error(f"No se encontró el archivo: {archivo}")