<h1 align="center"> Análisis de MOOCs para la toma de decisiones de una nueva Startup de tecnología </h1>

<p align="center">
   <img src="https://img.shields.io/badge/STATUS-%20FINALIZADO-green">
   </p>

<p align="center">
  <img width="700" height="280" src="Images/mooc_1.png">
</p>

# Tabla de contenidos
* [Introducción](#Introducción)

* [Decripción del proyecto](#Descripción-del-proyecto)

* [Descripción del problema](#Descripción-del-problema)

* [Propuesta de trabajo](#Propuesta-de-trabajo)

* [Desarrollo del proyecto](#Desarrollo-del-proyecto)

* [KPIs](#KPIs)

* [Principales tecnologías utilizadas](#Principales-tecnologías-utilizadas)

* [Información del proyecto](#Información-del-proyecto)

* [Conclusiones](#Conclusiones)

# Introducción
Hola a todos, hoy quiero compartirles un proyecto enfocado en el área de Data Analyst en el cual se van a explorar y analizar los rendimientos en ventas de tres plataformas de cursos online para la toma de decisiones de una nueva Startup de tecnología que quiere sumarse al mercado. 
# Descripción del proyecto

### *Cursos masivos abiertos y online*

Los MOOCs (cursos masivos abiertos y online, por sus siglas en inglés) han revolucionado el mundo de la educación desde principios de la década pasada, cuando el profesor Sebastian Thrun comenzó con la transmisión online de su curso introductorio a la Inteligencia Artificial. Poco tiempo después, Thrun fundó Udacity y con el pasar de los años se han ido sumando otras plataformas como edX y Coursera, brindando servicios similares: acceso a contenido específico, de calidad y de manera práctica, desde la comodidad del hogar. Muchas de estas plataformas tienen contenido gratuito mientras que el modelo de negocio en general se basa ya sea en el pago de suscripciones recurrentes para acceso general o únicas, para acceder a certificaciones o a cursos premium. Con el aumento de la popularidad de los MOOCs, no solo han aparecido nuevas plataformas privadas como las mencionadas anteriormente, sino que también muchas universidades y organizaciones sin fines de lucro han sumado a la oferta haciendo el mercado mucho más competitivo. En este contexto, resulta imperante para cada plataforma, ajustar sus modelos de negocio, los cursos y el contenido que se ofrece en los mismos para lograr captar y retener a la mayor cantidad de clientes.

# Descripción del problema

Nuestra Project Manager se dirigió a nosotros con un nuevo ticket de trabajo. Una startup de tecnología está interesada en sumarse al mercado de cursos online, pero de una manera eficiente, por lo que compró datasets de posibles competidores para analizar y sacar conclusiones de los datos recolectados.

# Propuesta de trabajo

* Ellos solicitan segmentar los el nivel de ventas según precio, idioma, nivel y rating de cada curso para analizar qué tanto influyen dichas variables en la demanda del producto vendido.

* Por otra parte se nos solicita un WordCloud de las palabras clave que más se repiten dentro del título. (Se puede añadir otras variables de nuestro interés).

* Con el fin de monitorear la eficacia de los objetivos de la empresa, se le pide establecer al menos 1 KPI producto de su análisis y que el mismo se pueda visualizar en un dashboard.

* Por último, se nos pide una demo en un rango de tiempo de no más de 10 min donde presentamos las funcionalidades del dashboard y las conclusiones/recomendaciones de nuestra parte.

# Desarrollo del proyecto

* Fuentes.

    Cargamos los datos dados en python los cuales se encuentran en el       siguiente link https://drive.google.com/drive/folders/1TS76ok6giW7D_l5vc-   zu5-cBU_dH3P5H.

* EDA.

    Realizamos distintas transformaciones como borrar nulos, imputar valores faltantes y outliers. Así mismo se crearon columnas necesarias para el análisis y se complementa con salidas gráficas de los datos para tener una mayor vision de nuestros datos.

* Power Bi.

    Cargamos nuestros datos limpios a Power Bi, sin embargo aún habian algunos errores de tipo de las columnas así que borramos los errores y procedemos a realizar tres dashboard con información de cada una de las tres plataformas: Udemy, EdX y Coursera.

*Word cloud
    Creamos una nube de plabras en python la cual nos muestra las plabras que más se repiten en los titulos de los cursos de los datasets dados.


## KPIs

* `Número de estudiantes inscriptos por curso, cursos más populares.` Este KPI nos permite ver qué cursos son los más solicitados por los usuarios de internet.
* `Número de cursos por área, áreas más populares.` Este KPI nos permite saber cuales son las áreas que más tienen crecimiento en el mundo de los cursos online. 


## Principales tecnologías utilizadas

* Python
    + pandas
    + seaborn
    + matplotlib
    + wordcloud
    + langdetect
* Power BI
    * DAX
    * Power Query

## Información del proyecto
Puede encontrar toda la información inicial de este proyecto en: https://github.com/soyHenry/PI03-Analytics.git

## Conclusiones:

Los cursos masivos abiertos y online han tenido un gran auge en los últimos tiempos  además de que instituciones y universidades se han sumado a dicho mundo. Actualmente los cursos más demandados y con mayor número de ventas son los cursos enfocados a áreas como Computación y ciencias, desarrollo web y Finanzas. Así, mismo podemos concluir que los cursos que generan un mayor ingreso se encuentran en el idioma Inglés.

Gracias por haber llegado hasta aquí 💛.
