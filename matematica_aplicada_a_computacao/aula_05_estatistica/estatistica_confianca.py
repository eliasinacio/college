# Calcular a  confiança

N = 20000   # população
e = 0.02    # margem de erro

n = N / (1 + N * e**2)

print(f'Tamanho da amostra {n}')