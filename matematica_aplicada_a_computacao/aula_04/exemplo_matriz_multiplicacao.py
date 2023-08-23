# Multiplicar as matrizes A e B

# A: [[3, 1, 3], [6, 5, 5]]
# B: [[100, 50], [50, 100], [50, 50]]

import numpy as np

a = np.array([[3, 1, 3], [6, 5, 5]])
b = np.array([[100, 50], [50, 100], [50, 50]])

result = np.matmul(a, b)

print('Resultado: \n', result)