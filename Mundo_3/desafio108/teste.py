# DESAFIO 108
# ADAPTE O CÓDIGO DO DESAFIO #107, CRIANDO UMA FUNÇÃO ADICIONAL CHAMADA MOEDA() 
# QUE CONSIGA MOSTRAR OS NÚMEROS COMO UM VALOR MONETÁRIO FORMATADO.

import moeda

print('\n\033[34m====== DESAFIO 108 ======\n\033[m')

p = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(p,10))}')
print(f'Reduzindo 13%, temos {moeda.moeda(moeda.diminuir(p,13))}')
