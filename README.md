
# 📊 Python CSV Statistics

Proyecto desarrollado durante el Máster en Big Data e Inteligencia Artificial para practicar el análisis y procesamiento de datos con Python.

## 📌 Descripción

Este proyecto implementa una herramienta para analizar ficheros CSV que contienen variables numéricas y categóricas.

El programa permite realizar un análisis inicial del dataset, gestionar valores ausentes representados mediante `?`, calcular diferentes estadísticas descriptivas y generar visualizaciones.

## 🛠️ Tecnologías utilizadas

- Python
- Pandas
- Matplotlib

## 🔍 Funcionalidades

El programa permite:

- Obtener el número de filas y columnas del dataset.
- Contar el número total de valores válidos.
- Detectar automáticamente columnas numéricas y categóricas.
- Calcular la media de variables numéricas.
- Obtener la moda de variables categóricas.
- Calcular la desviación estándar.
- Contar valores distintos.
- Obtener valores mínimos y máximos.
- Contar valores válidos por columna.
- Generar histogramas para variables numéricas.
- Generar gráficos circulares para variables categóricas.

## ▶️ Cómo ejecutar el programa

El programa se ejecuta desde la terminal indicando el fichero CSV y las opciones de análisis:

```bash
python estads.py nombre_fichero.csv opciones
