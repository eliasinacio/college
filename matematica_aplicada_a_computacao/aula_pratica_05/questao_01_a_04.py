# 1. Uma série de TV teve 10 episódios com as seguintes durações, em minutos:
#   35, 34, 26, 32, 37, 28, 27, 33, 36, 32.
#   Qual foi a duração média de cada episódio?

# 2. ... Qual foi a moda?
# 3. ... Qual foi a mediana?
# 4. ... Por meio do Python, obtenha a média, a moda e a mediana dos dados.

# rol = [26, 27, 28, 32, 32, 33, 34, 35, 37, 36]

media = (26 + 27 + 28 + 32 + 32 + 33 + 34 + 35 + 37 + 36) / 10
moda = 32
mediana = (32 + 33) / 2

print(f'1. Média: {media}')
print(f'2. Moda: {moda}')
print(f'3. Mediana: {mediana}')

# Trabalhar com dados no python também pode ser assim:

import pandas

rol = {'tempo': [26, 27, 28, 32, 32, 33, 34, 35, 37, 36]}

dados = pandas.DataFrame(rol)

media = dados['tempo'].mean()
moda = dados['tempo'].mode()
mediana = dados['tempo'].median()

print(f'4. \nMédia: {media} \nModa: {moda} \nMediana: {mediana}')