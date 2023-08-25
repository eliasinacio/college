# 9/10. Utilizando a fórmula de Slovin (10. e o python), qual é o tamanho da amostra referente a 
#   uma população de 200.000 dados considerando uma margem de erro de 4%?

from math import ceil

N = 200000
e = 0.04

n = ceil(N / (1 + N * e**2))  # fórmula de Slovin

print(f'{n}')