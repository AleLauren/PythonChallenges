# DESAFIO 107
# CRIE UM MÓDULO CHAMADO MOEDA.PY QUE TENHA AS FUNÇÕES INCORPORADAS 
# AUMENTAR(), DIMINUIR(), DOBRO() E METADE(). 
# FAÇA TAMBÉM UM PROGRAMA QUE IMPORTE ESSE MÓDULO E USE ALGUMAS DESSAS FUNÇÕES.

import moeda

print('\n\033[34m====== DESAFIO 107 ======\n\033[m')

p = float(input('Digite o preço: R$'))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'Aumentando 10%, temos {moeda.aumentar(p,10)}')
print(f'Reduzindo 13%, temos {moeda.diminuir(p,13)}')
