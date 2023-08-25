# 8. O tempo médio para a chegada de uma ambulância no local onde precisa prestar atendimento tem média de 15 minutos após o chamado com desvio padrão de 3 minutos. 
#   Sabendo que os tempos estão de acordo com uma distribuição normal, qual é a probabilidade de que uma ambulância chegue entre 10 e 15 minutos?

desvioPadrao = 3
media = 15
x = 10

# Distribuição normal

distribuicaoNormal = (x - media) / desvioPadrao

print(f'Distribuicão Normal: {distribuicaoNormal:.2f} %')

# Na tabela de Distribuição normal a probabilidade associada a 1.67 é 0.4525

probabilidade = 0.4525 * 100

print(f'Probabilidade: {probabilidade} %')