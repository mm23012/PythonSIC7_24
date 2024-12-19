# Análisis de Criptomonedas: Herramientas para la transparencia y la toma de decisiones

El proyecto esta desarrollado en el lenguaje Python donde se realiza un analisis detallado sobre las criptomonedas, desde la visualización de precios a traves del tiempo 
hasta una comparación entre estas mismas. Todo esto siendo accesible desde un menú interactivo.


## Tabla de contenidos

1. [Nombre](#Nombre)
2. [Descripción](#descripción)
3. [Arquitectura](#Arquitectura)
4. [Proceso](#Proceso)
5. [Funcionalidades](#Funcionalidades)

* Análisis de Criptomonedas: Herramientas para la transparencia y la toma de decisiones

* El proyecto esta desarrollado en el lenguaje Python donde se realiza un analisis detallado sobre las criptomonedas, desde la visualización de precios a traves del tiempo 
hasta una comparación entre estas mismas. Todo esto siendo accesible desde un menú interactivo.

![proyecto](https://github.com/user-attachments/assets/c7c4135c-1fae-4e18-99d2-3fe1665bb4b0)

* Arquitectura:

  ![arquitectura](https://github.com/user-attachments/assets/ab723dee-595a-4c37-b840-112503cfdf2c)

* Proceso de desarrollo:

- Fuente del dataset:

Adopcion de Criptomonedas:
https://www-triple--a-io.translate.goog/cryptocurrency-ownership-data?_x_tr_sl=en&_x_tr_tl=es&_x_tr_hl=es&_x_tr_pto=tc

PIB per capita:
https://datos.bancomundial.org/indicador/NY.GDP.PCAP.CD?locations=VC

Valor de monedas:

https://es.investing.com/currencies/usd-jpy-historical-data

https://es.investing.com/currencies/cny-usd-historical-data

https://es.investing.com/currencies/chf-usd-historical-data

https://es.investing.com/currencies/eur-usd-historical-data


- Limpieza de datos:

![limpieza](https://github.com/user-attachments/assets/e755de59-0c1c-40b0-84b6-3dc12d41d55d)


- Manejo excepciones/control errores:
Se manejan excepciones al momento de filtrar los datos en la función de cargar_datos y en opciones donde el usuario deba de elegir una opción, principalmente en las opciones de ver los tipos de gráficos.

![excepcion1](https://github.com/user-attachments/assets/086e8593-8091-4055-a7c1-25118fd5fdb0)

![excepcion2](https://github.com/user-attachments/assets/878a77f9-9e63-4711-8f0f-25ab150b6b5a)


- Estadísticos:
Graficos tipo Lineal, Boxplot, ScatterPlot

Grafico de Correlación sobre la integración Social

Graficos comparativos de las principales criptomonedas en un año en especifico

Grafico de precios de criptomoneda especifica

* Funcionalidad extra:

Menú interactivo para acceder a los distintos gráficos.
- Funciones básicas del lenguaje de programación Python (print(), input())
- Arquitectura:
  
  ![menu](https://github.com/user-attachments/assets/7466f44a-34ec-404c-90af-f58f8323f6d1)

