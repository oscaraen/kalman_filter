# Script de ejemplo para el manejo de filtros de kalman (Kalman filter premier)

import numpy as np

muestras = 1000
ruidosa = np.random.normal(0.8624, 0.2,muestras)
Sm = np.mean(ruidosa)
Sdv = np.std(ruidosa)

# Espacio de estados del modelo
Q = 1e-5
R = np.power(Sdv, 2)

X = np.zeros(1, muestras)
P = np.zeros(1, muestras)
# esperar a la clase de Kalman para ver cómo se llena esto, subir el repo a Github para compartir con el portatil

