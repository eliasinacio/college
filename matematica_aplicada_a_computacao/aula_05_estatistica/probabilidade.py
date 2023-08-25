# calcular a pribabilidade acima da média
import scipy.stats

media = 000
desvioPadrao = 000
x = 000

p = scipy.stats.norm(media, desvioPadrao).cdf(x) - 0.5

print(p)

# calcular a pribabilidade abaixo da média
import scipy.stats

media = 000
desvioPadrao = 000
x = 000

p = 0.5 - scipy.stats.norm(media, desvioPadrao).cdf(x)

print(p)