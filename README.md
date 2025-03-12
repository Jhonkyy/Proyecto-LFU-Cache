# **Proyecto: Implementación de una Caché LFU**

## **Descripción General**

El objetivo de este proyecto es diseñar e implementar una caché de tipo **LFU (Least Frequently Used)** utilizando una combinación de **listas ligadas** y un **diccionario hash** para optimizar la eficiencia en el acceso a los datos almacenados. Este proyecto permitirá a los estudiantes comprender estructuras de datos avanzadas y su aplicación en escenarios reales, como la optimización de sistemas de almacenamiento en memoria y la gestión de datos en bases de datos y servidores web.

## **¿Qué es una Caché LFU?**

Una **caché LFU (Least Frequently Used)** es una estructura de datos utilizada para almacenar un número
limitado de elementos, priorizando aquellos que han sido accedidos con mayor frecuencia. Cuando la caché
alcanza su límite de capacidad, elimina el elemento que ha sido usado con menor frecuencia.

La implementación clásica de una caché LFU usa:

- **Diccionario (Hash Table):** para permitir acceso rápido a los elementos almacenados en la caché.

- **Lista Ligada de Frecuencias:** para organizar los elementos en grupos según la cantidad de veces que
han sido accedidos.
