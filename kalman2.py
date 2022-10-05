"""
Uso de un filtro de Kalman con la librería filterpy

En este caso se pretende resolver un problema de seguimiento de un voltaje que cambia dada una función a trozos
"""
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')

# generando una señal con un cambio en dos dimensiones para el filtro de Kalman
n_samples = 1500
x_space = np.linspace(0, 10, n_samples)
fase1 = np.ones(500) * 3  # iniciar en 3v
fase2 = x_space[500:800] *0.2 + 2.8
fase3 = x_space[800:1000] * 0.8 - 2
fase4 = np.ones(500) * 8
clean_signal = np.concatenate([fase1, fase2, fase3, fase4])

plt.plot(x_space, clean_signal)
plt.xlabel("tiempo")
plt.ylabel("espacio")
plt.grid()
plt.show()