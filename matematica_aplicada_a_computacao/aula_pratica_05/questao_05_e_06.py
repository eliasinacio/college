# 5. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
#   35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
#   Por se tratar de um conjunto com poucos dados, calcule a variância amostral e o desvio padrão amostral.

dados = [35, 34, 26, 32, 37, 28, 27, 33, 36, 32]
n = len(dados)

somatorio = 0

for x in dados:
    somatorio += (x - 32) ** 2

varianciaAmostral = somatorio / n - 1
desvioPadraoAmostral = (somatorio / n - 1) ** (1/2)

print(f'Variância amostral: {varianciaAmostral}')
print(f'Desvio Padrão amostral: {desvioPadraoAmostral:.2f}')