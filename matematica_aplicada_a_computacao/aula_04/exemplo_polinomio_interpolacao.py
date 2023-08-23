# Obter o polinômio que interpola os pontos A(4, 2), B(7, -1), C(10, 12) e D(11, 15)

from scipy.interpolate import *

x = [4, 7, 10, 11]      # pontos x
y = [2, -1, 12, 15]     # pontos y

p = lagrange(x, y)

print(p)