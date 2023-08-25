# Considere um projetor multimídia cuja lâmpada tem vida útil 
#   de 5000 horas com desvio padrão de acordo com uma ditribuição normal.
#   Determine, por meio do python, a probabilidade de que um projetor seleciionado ao acaso, 
#   tenha lâmpada com vida útil entre 5000 e 5500 horas.

import scipy.stats

media = 5000
desvioPadrao = 300
x = 5500                # acima da média

p = scipy.stats.norm(media, desvioPadrao).cdf(x) - 0.5

print(p)