# Script de ejemplo para el manejo de filtros de kalman (Kalman filter premier) para cambios en la señal de entrada
# en este caso se hace para una señal sinusoidal la cual se hace el seguimiento
# con la misma política de random walk (la mejor estimación es la pasada, no hay modelo)

# dependiendo del valor de Q (mas o menos confianza en el modelo) me ajusto mejor o no a los datos
# el filtro aprende la velocidad de cambio según eso
import matplotlib.pyplot as plt
import numpy as np
f1 = 8
f2 = 20
n_samples = 2000
desv_est = 0.0001
samples1 = np.linspace(0, np.pi/5, n_samples//2)
samples2 = np.linspace(np.pi/5, 2*np.pi/5, n_samples//2)
x_space = np.concatenate([samples1, samples2])
y1 = np.sin(2*np.pi*f1*samples1)
y2 = np.sin(2*np.pi*f2*samples2)
samples_clean = np.concatenate((y1, y2))
# add noise to samples
samples = samples_clean + np.random.normal(0,0.04,n_samples)
Sm = np.mean(samples)
Sdv = np.std(samples)

# Espacio de estados del modelo
Q = 1e-1  # por experiencia se escoge la del proceso pequeña (pero mas grande que la real para que la abarque)
R = np.power(Sdv, 2)  # varianza del sensor R, varianza del sensor al cuadrado

X = np.zeros((n_samples))
print(X.shape)
P = np.zeros((n_samples))
# esperar a la clase de Kalman para ver cómo se llena esto, subir el repo a Github para compartir con el portatil

Xposterior = 0  # asumir un valor inicial de las cosas, le digo en donde empiece, o el primer dato del sensor.
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
plt.scatter(x_space,samples, color="gray", marker=".", s=4)
plt.plot(x_space, X, color="green") # filtro de kalman en verde
#plt.plot(samples, color="red") # ground truth
plt.grid()
plt.title("2Corrección de mediciones con filtro de Kalman")
plt.legend(["Sensor pailas", "Filtrada"])
plt.xlabel("muestras")
plt.ylabel("Variable medida")
plt.text(0, -2, f'Q={Q}, R={R}', fontsize=14)
plt.show()

# probar con ruidos mayores para validar el comportamiento del sistema