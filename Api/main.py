# Se importan todas las librerias a utilizar.
from fastapi import FastAPI
import pandas as pd
import uvicorn
import numpy as np
from typing import Optional
from typing import List, Tuple


# Se crea la app donde se realizarán las consultas.
app = FastAPI(title = 'Streaming Services')

df = pd.read_csv('Dataset\plataformas.csv')

@app.get("/")
async def index():
    return "Hola! aqui puedes realizar consultas plataformas de streaming, para mas informacion ir a /docs"

# http://127.0.0.1:8000/docs#/

#1. Película (sólo película, no serie, etc) con mayor duración según año, plataforma y tipo de duración.

@app.get("/get_max_duration/{anio}/{plataforma}/{dtype}")

def get_max_duration(year: int, platform: str, duration_type: str):
    # Filtrar el DataFrame
    df_filtered = df[(df['release_year'] == year) & (df['plataforma'] == platform) & (df['duration_type'] == duration_type) & (df['type'] == 'movie')]

# Verificar si el DataFrame filtrado está vacío o si hay valores nulos en la columna de duración
    if df_filtered.empty or df_filtered['duration_int'].isna().any():
        return "No disponible: la pelicula no se encuentra con esas especificaciones"
    
    # Ordenar las filas por duración
    df_sorted = df_filtered.sort_values('duration_int', ascending=False)

    # Tomar el nombre de la primera fila (la película con la duración más larga)
    movie_name =  df_sorted.iloc[0]['title']

    return 'La pelicula con mayor duración esta plataforma es:'+ movie_name

# http://127.0.0.1:8000/get_max_duration/{year, platform, duration_type}?year=2020&platform=hulu&duration_type=min

# 2. Cantidad de películas (sólo películas, no series, etc) según plataforma, 
# con un puntaje mayor a XX en determinado año. La función debe llamarse get_score_count(platform, scored, year) y 
# debe devolver un int, con el total de películas que cumplen lo solicitado.

@app.get("/get_score_count/{platform}/{scored}/{year}")

def get_score_count(platform: str, scored: float, year: int):
    movies_platform_year = df.loc[(df['type'] == 'movie') & (df['plataforma'] == platform) & (df['release_year'] == year)]
    movie_count = movies_platform_year.loc[movies_platform_year['rating_y'] > scored]['id'].count()
    return  f'en la plataforma y scored ingresada hay un total de : {movie_count} películas'

# http://127.0.0.1:8000/get_score_count/{platform, scored, year}?platform=disney&scored=3.2&year=2011

# 3. Cantidad de películas (sólo películas, no series, etc) según plataforma. 
# La función debe llamarse get_count_platform(platform) y debe devolver un int, 
# con el número total de películas de esa plataforma. Las plataformas deben llamarse amazon, netflix, hulu, disney.

@app.get("/get_count_platform/{platform}")
def get_count_platform(platform: str):
    # filtrar filas que corresponden a películas y la plataforma especificada
    movies = df[(df['type'] == 'movie') & (df['plataforma'] == platform)]
   
    return f'En esta plataforma existen {len(movies)} películas'

# http://127.0.0.1:8000/get_count_platform/amazon

# 4. Actor que más se repite según plataforma y año. La función debe llamarse get_actor(platform, year) y 
# debe devolver sólo el string con el nombre del actor que más se repite según la plataforma y el año dado.

@app.get("/get_actor/{platform}/{year}")
def get_actor(platform: str, year: int):
    df_filtered = df[(df['plataforma'] == platform) & (df['release_year'] == year)]
    actor_count = {}
    for actors in df_filtered['cast']:
        if isinstance(actors, str):
            for actor in actors.split(','):
                actor_count[actor.strip()] = actor_count.get(actor.strip(), 0) + 1
    if len(actor_count) == 0:
        return "No se encontraron actores"
    else:
        return 'Actor que más se repite según la plataforma y año:  ' + max(actor_count, key=actor_count.get)

# http://127.0.0.1:8000/get_actor/{platform, year}?platform=amazon&year=2014

# 5. La cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año.

@app.get("/prod_per_county/{tipo}/{pais}/{anio}")
def prod_per_county(tipo: str, pais: str, anio: int):

    filtro = df[(df['type'] == tipo) & (df['country'].str.contains(pais)) & (df['release_year'] == anio)]
   
    cantidad = len(filtro)
    resultado = {'La cantidad de contenidos que se publicó para ': pais, 'en el anio': anio, tipo: cantidad}
    return resultado

#http://127.0.0.1:8000/prod_per_county/{tipo, pais, anio}?tipo=movie&pais=argentina&anio=2020

# 6. La cantidad total de contenidos/productos  según el rating de audiencia dado (para que publico fue clasificada la pelicula).
@app.get("/get_contents/{rating}")
def get_contents(rating: str):
   
    df_filtered = df[df['rating_x'] == rating]
  
    count = len(df_filtered)
    
    return f'cantidad total de contenidos según el rating de audiencia dado es:  {count}'
# http://127.0.0.1:8000/get_contents/tv-g

