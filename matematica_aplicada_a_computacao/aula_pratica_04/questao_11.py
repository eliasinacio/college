# 11. Construa o gráfico da função y=x³-2x²+12x-1 no intervalo [-3, 4].

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 4, 100)

f = x**3 - 2*x**2 + 12*x - 1

plt.plot(x, f)
plt.show()