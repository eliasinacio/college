# Uma indústria de cadeiras gamer possui três modelos denominados de A, B e C, e possui duas fábricas chamadas de F1 e F2. 
# Na fábrica F1, são produzidas as peças, e na fábrica F2 é feita a montagem das cadeiras.
# Ambas possuem seus custos além do custo de transporte

#  F1: custo | transporte
# A: 400 | 10
# B: 480 | 12
# C: 600 | 15

#  F2: custo | transporte
# A: 31 | 11
# B: 37 | 11
# C: 48 | 11

import numpy as np

f1 = np.array([[400, 10], [480, 12], [600, 15]])
f2 = np.array([[31, 11], [37, 11], [48, 11]])

total = f1 + f2

print('Custos totais: \n', total)

f1 = 1.1*f1

print('\nCustos f1 com 10% de acréscimo: \n', f1)