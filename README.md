# PI_ML_OPS_Henry.1
# Este proyecto está dedicado a la descarga, pre-preparación, procesamiento de datos y desarrollo de una API que  disponibilice la información de la empresa.

 **Acceso a la documentación en render.com [https://startup-de-servicios-de-streaming.onrender.com/docs](https://startup-de-servicios-de-streaming-gh7h.onrender.com/docs#/)**   desde donde podrás acceder a todas las consultas desarrolladas.
 
 Propuesta de trabajo:
 **Transformaciones: [Link](https://github.com/Yina-sanchez/PI_ML_OPS_Henry.1/blob/main/ETl_plataformas_stremer.ipynb)

 * Generar campo id: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets 

 * Los valores nulos del campo rating deberán reemplazarse por el string “G” (corresponde al maturity rating: “general for all audiences”

 * De haber fechas, deberán tener el formato AAAA-mm-dd

 * Los campos de texto deberán estar en minúsculas, sin excepciones

 * El campo duration debe convertirse en dos campos: duration_int y duration_type. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)
 
 **Desarrollo API: Propones disponibilizar los datos de la empresa usando el framework FastAPI, generando diferentes endpoints que se consumiran en la API. [Link](https://github.com/Yina-sanchez/PI_ML_OPS_Henry.1/blob/main/API.ipynb)
 
 **Análisis exploratorio de los datos: (Exploratory Data Analysis-EDA) [Link](https://github.com/Yina-sanchez/PI_ML_OPS_Henry.1/blob/main/EDA_plataformas.ipynb)
 
 **Sistema de recomendación   [Link](https://github.com/Yina-sanchez/PI_ML_OPS_Henry.1/blob/main/ML_sistema_recomendacion.ipynb)
 * Éste consiste en recomendar películas a los usuarios basándose en películas similares, por lo que se debe encontrar la similitud de puntuación entre esa película y el resto de películas, se ordenarán según el score y devolverá una lista de Python con 5 valores
 
 [**Video ExplicaciExplicación**]()
 
 # Consulta de las funciones 

  1. Función **get_max_duration**: película con mayor duración con filtros opciones de Año, Plataforma y Tipo de Duración.
  
     Consulta #1 [Link get_max_duration](https://startup-de-servicios-de-streaming-gh7h.onrender.com/get_max_duration/%7Banio%7D/%7Bplataforma%7D/%7Bdtype%7D?year=2021&platform=hulu&duration_type=min)

 2. Función **get_score_count**: cantidad de películas por plataforma con un puntaje mayor a determinado número en determinado año.
     
     Consulta #2 [Link get_score_count](https://startup-de-servicios-de-streaming-gh7h.onrender.com/get_score_count/disney/3.2/2011)
 
 3. Función **get_count_platform**: cantidad de películas según la plataforma.

    Consulta #3 [Link get_count_platform](https://startup-de-servicios-de-streaming-gh7h.onrender.com/get_count_platform/amazon)
 
 4. Función **get_actor**: actor que mas se repite según plataforma y año.
 
    Consulta #4 [Link get_actor](https://startup-de-servicios-de-streaming-gh7h.onrender.com/get_actor/amazon/2014)

 5. Función **prod_per_county** Cantidad de contenidos/productos (todo lo disponible en streaming) que se publicó por país y año.

    Consulta #5 [Link prod_per_county](https://startup-de-servicios-de-streaming-gh7h.onrender.com/prod_per_county/movie/argentina/2020)

 6. Función **get_contents** Cantidad total de contenidos/productos  según el rating de audiencia dado (para que publico fue clasificada la pelicula).
   
    Consulta #6 [Link get_contents](https://startup-de-servicios-de-streaming-gh7h.onrender.com/get_contents/tv-g)
  
 7. Función **get_recommendation** Sistema de recomendación
    
    Consulta #7 [Link get_recommendation](https://startup-de-servicios-de-streaming-gh7h.onrender.com/get_recommendation/sing%20and%20dance%20with%20kiiyii)
    
