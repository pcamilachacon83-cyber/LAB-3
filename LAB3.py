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



