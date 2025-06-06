# -*- coding: utf-8 -*-
"""modelos_no_supervisados_clustering_k-means

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1amVrjcuKx42p9OOu_q_G5HvFBfxKkXga

1. Importamos las librerías

*   scikit-learn
*   numpy
*   matplotlib
"""

from sklearn.cluster import KMeans
import numpy as np
import matplotlib.pyplot as plt

"""2. Definir el conjunto de datos

Creamos un conjunto de datos de ejemplo que consiste en puntos en un espacio bidimensional (coordenadas X e Y). Cada par de números en el array representa un punto.
"""

X = np.array([[1, 2], [1, 4], [1, 0], [4, 2], [4, 4], [4, 0],
              [5, 1], [3, 3], [2, 5], [6, 3], [7, 2], [8, 0],
              [9, 3], [10, 4], [8, 5], [6, 6], [9, 7], [11, 1],
              [12, 4], [13, 2], [12, 6], [14, 5], [15, 3], [14, 7]])

"""3. Instanciamos al modelo K-means

**KMeans(n_clusters=4)**: Esto indica que queremos dividir los datos en 4 grupos o clusters. El número de clusters es un parámetro importante que debe ser definido antes de entrenar el modelo.

**random_state=0**: Esto se utiliza para hacer que el algoritmo sea reproducible, ya que K-means inicializa los centroides aleatoriamente. Fijar la semilla permite que obtengamos los mismos resultados cada vez que ejecutemos el código.

**.fit(X)**: Este comando entrena el modelo de K-means usando el conjunto de datos X. Durante este proceso, el algoritmo ajusta los centroides y asigna cada punto al cluster más cercano.
"""

kmeans = KMeans(n_clusters=4, random_state=0)
kmeans.fit(X)

"""4. Obtenemos las etiquetas (clusters)

labels_: Después de entrenar el modelo, esta propiedad almacena la asignación de cada punto al cluster correspondiente. Por ejemplo, si el primer punto pertenece al cluster 0 y el segundo al cluster 1, los valores de labels_ serán [0, 1, ...].
"""

labels = kmeans.labels_
labels

"""5. Obtenemos los Centroides

cluster_centers_: Después del proceso de clustering, esta propiedad almacena las coordenadas de los centroides calculados por K-means. Recordemos que los **centroides** son el promedio de los puntos en cada cluster y representan el "centro" de los clusters.
"""

centroids = kmeans.cluster_centers_
centroids

"""6. Visualización

**plt.scatter(X[:, 0], X[:, 1], c=labels)**: grafica los puntos del conjunto de datos en un gráfico de dispersión (scatter plot). Utiliza las coordenadas X e Y de cada punto, y colorea los puntos según su cluster (almacenado en labels).

**plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')**: agrega los centroides a la gráfica. Los centroides se mostrarán como marcas rojas ("x") en el gráfico.

**plt.show()**: Muestra el gráfico final.
"""

plt.scatter(X[:, 0], X[:, 1], c=labels)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', marker='x')
plt.show()

"""7. Interpretación

El gráfico resultante muestra cuatro grupos de puntos que representan los **clusters**. Los puntos de un mismo color pertenecerán al mismo cluster.

Los **centroides** estarán marcados con una "x" roja, representando el centro de cada cluster según lo calculado por el algoritmo de K-means.
"""