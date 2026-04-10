# transporte-masivo-no-supervisado# Actividad 6 – Aprendizaje No Supervisado (K-Means)

**Estudiante:**  Yeraldin Arboleda Quintero
**Fecha:** abril 2026  
**Capítulo:** 16 – Técnicas de agrupamiento

## Descripción

Este proyecto aplica el algoritmo **K-Means** para agrupar rutas de transporte masivo según:
- Distancia recorrida (km)
- Velocidad promedio (km/h)
- Número de pasajeros

El dataset es sintético y contiene 12 rutas.

## Archivos en el repositorio

| Archivo | Descripción |
|---------|-------------|
| `transporte_no_sup.csv` | Datos de entrada (hora, distancia, velocidad, pasajeros) |
| `modelo_kmeans.py` | Código Python que entrena K-Means y genera clusters |
| `descripcion_datos.txt` | Explicación de las columnas del dataset |
| `pruebas.txt` | Resultados y análisis de los clusters obtenidos |
| `resultados_clusters.csv` | Archivo generado con la asignación de cada ruta a un cluster |

## Ejecución

```bash
python modelo_kmeans.py

