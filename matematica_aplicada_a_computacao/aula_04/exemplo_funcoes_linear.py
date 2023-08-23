# f(x) = 28x

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)    # Gera um vetor com 100 valores entre 0 e 10

f = 28*x         # função

plt.plot(x, f)   # gera um gráfico
plt.show()       # mostra o gráfico