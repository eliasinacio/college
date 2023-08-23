# 10. Considere as matrizes
#    A: [[3, 5, 9], [4, 2, -3], [1, 5, -5]]
#    B: [[12, -6, 7], [3, 0, 2], [-1, 10, 1]]

# Utilize o Python para obter a matriz C=A.B.

import numpy as np

a = np.array([[3, 5, 9], [4, 2, -3], [1, 5, -5]])
b = np.array([[12, -6, 7], [3, 0, 2], [-1, 10, 1]])

c = np.matmul(a, b)

print(c)