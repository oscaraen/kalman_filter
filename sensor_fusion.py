"""
Script para la simulación del ejercicio de fusión de datos. En este caso se tiene un proceso con un horno (smilar a pasteurización de leche)
Y se tienen tres sensores, una RTD, una NTC y una Termocupla. La simulación se hace en el orden de los segundos de un proceso que dura
90 minutos. (Hacer pasos de 1 segundo).

Se utlizarán 3 distribuciones e incluso datos atípicos que puedan ocurrir para simular con éxito t.odo el proceso.

Para el caso de los sensores utilizar Kallendar van dussen (modelo no lineal)
Para el caso del NTC steinhart-hart
Para el caso de la termocupla un polinomio

Usar la ley de calentamiento y enfriamiento de newton para poder


Nota: en el caso de la termocupla, hay varianza homosedástica y heterosedástica, es decir, en cierto rango de temperatura es
un error y en otro rango el error cambia. por tanto R cambia.



"""



import numpy as np
import matplotlib.pyplot as plt


