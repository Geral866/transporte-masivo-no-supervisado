import pandas as pd
from sklearn.cluster import KMeans

data = pd.read_csv('transporte_no_sup.csv')
X = data[['distancia_km', 'velocidad_kmh', 'pasajeros']]

kmeans = KMeans(n_clusters=3, random_state=42)
data['cluster'] = kmeans.fit_predict(X)

print(data)
print("\nCentroides:")
print(kmeans.cluster_centers_)

data.to_csv('resultados_clusters.csv', index=False)
print("\nresultados_clusters.csv generado correctamente.")
