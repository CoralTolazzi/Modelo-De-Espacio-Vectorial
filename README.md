# Trabajo Práctico N.º 8 - Modelo de Espacio Vectorial

**Nombre:** Coral Tolazzi
**Materia:** Procesamiento del Lenguaje Natural
**Tema:** Recuperación de la Información
**Profesora:** Yanina Ximena Scudero
**Cuatrimestre:** 1.º Cuatrimestre del 2025
**Instituto:** Instituto Tecnológico Beltrán

## Descripción

Este trabajo práctico consiste en la implementación de un modelo de espacio vectorial para medir la similitud entre documentos utilizando **TF-IDF** y **similitud del coseno**. El objetivo es aplicar técnicas de representación numérica de texto y visualización para evaluar qué tan similares son distintos documentos entre sí.

## Funcionalidades

* Representación vectorial de documentos con la técnica **TF-IDF**.
* Cálculo de **similitud del coseno** entre pares de documentos.
* Visualización de la **matriz de similitud** mediante un **mapa de calor**.
* Análisis visual e interpretativo de resultados de similitud semántica.

## Documentos Analizados

```text
doc1: "El veloz zorro marrón salta sobre el perro perezoso."
doc2: "Un perro marrón persiguió al zorro."
doc3: "El perro es perezoso."
```

Estos documentos se vectorizan y comparan entre sí para medir su nivel de similitud.

##  Pasos del Código

1. **Importación de librerías**

   * `matplotlib.pyplot`, `seaborn`: visualización.
   * `TfidfVectorizer`: vectorización TF-IDF.
   * `cosine_similarity`: medición de similitud.

2. **Definición de los documentos**
   Lista de textos que representan el corpus a analizar.

3. **Vectorización TF-IDF**
   Cada documento se transforma en un vector numérico donde cada componente representa el peso de una palabra.

4. **Cálculo de la similitud del coseno**
   Se obtiene una matriz 3x3 donde cada celda indica la similitud entre un par de documentos (valor entre 0 y 1).

5. **Visualización con heatmap**
   Se genera un gráfico de calor (heatmap) para visualizar la similitud entre documentos, usando tonos de azul y etiquetas claras.

## Resultado Esperado

Se obtiene una **matriz de similitud** (Resultado De La Matriz.png)

El gráfico correspondiente permite ver de forma visual cuál documento es más similar a cuál, facilitando el análisis semántico.

## Conclusión

Este trabajo práctico introduce el uso del **modelo vectorial de recuperación de información**, mostrando cómo representar textos con TF-IDF y cómo interpretar sus similitudes. Además, refuerza el uso de herramientas de visualización como `seaborn` para interpretar resultados de manera efectiva y visual.
