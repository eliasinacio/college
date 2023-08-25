import pandas as pd

x = {'pesos': [48.8, 48.9, 49, 49.1, 49.2, 49.3, 49.5, 49.7, 49.7, 49.8, 50, 50.1, 50.1, 50.2, 50.2, 50.4, 50.6, 50.9]}

p = pd.DataFrame(x)

desvioPadrao = p['pesos'].std()

print(f'Desvio-padrão: {desvioPadrao}')