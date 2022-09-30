# DESAFIO 109
# MODIFIQUE AS FUNÇÕES QUE FORM CRIADAS NO DESAFIO 107 
# PARA QUE ELAS ACEITEM UM PARÂMETRO A MAIS, 
# INFORMANDO SE O VALOR RETORNADO POR ELAS VAI SER OU NÃO 
# FORMATADO PELA FUNÇÃO MOEDA(), DESENVOLVIDA NO DESAFIO 108.

import moeda

print('\n\033[34m====== DESAFIO 109 ======\n\033[m')

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p,True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p,True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10,True)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13,True)}')
