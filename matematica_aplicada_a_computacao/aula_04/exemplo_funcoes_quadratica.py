# f(x) = -340x² + 5700x - 9500

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 100)

f = -340*x**2 + 5700*x - 9500

plt.plot(x, f)   # gera um gráfico
plt.show()       # mostra o gráfico