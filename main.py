# Script de ejemplo para el manejo de filtros de kalman (Kalman filter premier)
import matplotlib.pyplot as plt
import numpy as np

muestras = 1000
ruidosa = np.random.normal(0.8624, 0.2,muestras)
Sm = np.mean(ruidosa)
Sdv = np.std(ruidosa)

# Espacio de estados del modelo
Q = 1e-5 # por experiencia se escoge la del proceso pequeña (pero mas grande que la real para que la abarque)
R = np.power(Sdv, 2) # varianza del sensor R, varianza del sensor al cuadrado

X = np.zeros((1, muestras))
P = np.zeros((1, muestras))
# esperar a la clase de Kalman para ver cómo se llena esto, subir el repo a Github para compartir con el portatil

Xposterior = 0.8  # asumir un valor inicial de las cosas, le digo en donde empiece, o el primer dato del sensor.
Pposterior = 1

for i in range(len(ruidosa)):

    ym = ruidosa[i] # simular que acaba de llegar una medida
    # predict
    Xprior = Xposterior # mejor primer prior es el posterior
    Pprior = Pposterior + Q # asumiendo F = 1

    # update
    K = Pprior * 1/(Pprior + R) # H vale 1
    Xposterior = Xprior + K * (ym - Xprior)
    Pposterior = (1 - K) * Pprior

    # store result
    np.append(X, Xposterior)
    np.append(P, Pposterior)

plt.plot(muestras)
plt.plot(X) #
plt.plot(np.ones(muestras)*Sm) # ground truth

plt.show()
