# 6. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u+v utilizando o Python.
# 7. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u-v utilizando o Python.
# 8. Dados os vetores u=(3, 4, 8) e v=(10, 12, -1), obtenha o vetor u.v utilizando o Python.

import numpy as np

v1 = np.array([[3, 4, 8]])
v2 = np.array([[10, 12, -1]])

r06 = v1 + v2
r07 = v1 - v2
r08 = np.inner(v1, v2)  # multiplicação de vetores

print('06. \n', r06)
print('\n07. \n', r07)
print('\n08. \n', r08)