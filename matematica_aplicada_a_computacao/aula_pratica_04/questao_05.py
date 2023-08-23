# 5. O vetor v contém os preços de venda de algumas mercadorias: v=(1210, 897, 1230, 1495, 799, 890, 1010)
#    A loja está com uma promoção onde é dado um desconto de 20% em todas as
#    mercadorias. Por meio do Python, obtenha o vetor que contém os preços destas
#    mercadorias com o desconto.

import numpy as np

prices = np.array([[1210, 897, 1230, 1495, 799, 890, 1010]])
prices = prices * 0.8

print(prices)