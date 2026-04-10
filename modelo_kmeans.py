import pandas as pd
from sklearn.cluster import KMeans

# Cargar datos
data = pd.read_csv('transporte_no_sup.csv')
X = data[['distancia_km', 'velocidad_kmh', 'pasajeros']]

# Aplicar K-Means con 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

# Mostrar resultados
print("Datos con cluster asignado:")
print(data)
print("\nCentroides:")
print(kmeans.cluster_centers_)

# Guardar resultados
data.to_csv('resultados_clusters.csv', index=False)
print("\nArchivo 'resultados_clusters.csv' generado correctamente.")

