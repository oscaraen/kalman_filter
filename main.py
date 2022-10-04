# Script de ejemplo para el manejo de filtros de kalman (Kalman filter premier)
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')
import numpy as np

n_samples = 1000
samples = np.random.normal(0.8624, 0.04, n_samples)
Sm = np.mean(samples)
Sdv = np.std(samples)

# Espacio de estados del modelo
Q = 1e-7 # por experiencia se escoge la del proceso pequeña (pero mas grande que la real para que la abarque)
R = np.power(Sdv, 2) # varianza del sensor R, varianza del sensor al cuadrado

X = np.zeros((n_samples))
print(X.shape)
P = np.zeros((n_samples))
# esperar a la clase de Kalman para ver cómo se llena esto, subir el repo a Github para compartir con el portatil

Xposterior = 0.8  # asumir un valor inicial de las cosas, le digo en donde empiece, o el primer dato del sensor.
Pposterior = 1

for i in range(len(samples)):

    ym = samples[i]  # simular que acaba de llegar una medida
    # predict
    Xprior = Xposterior  # mejor primer prior es el posterior
    Pprior = Pposterior + Q  # asumiendo F = 1

    # update
    K = Pprior * 1/(Pprior + R)  # H vale 1
    Xposterior = Xprior + K * (ym - Xprior)
    Pposterior = (1 - K) * Pprior

    # store result
    X[i] = Xposterior
    P[i] = Pposterior

print(len(X))
plt.scatter(range(n_samples),samples)
plt.plot(X, color="green") # filtro de kalman en azul
plt.plot(np.ones(n_samples)*Sm, color="red") # ground truth

plt.show()
