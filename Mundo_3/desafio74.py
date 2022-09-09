# DESAFIO 074
# CRIE UM PROGRAMA QUE VAI GERAR CINCO NÚMEROS ALEATÓRIOS (DE 1 A 100)
# E COLOCAR EM UMA TUPLA. DEPOIS DISSO, MOSTRE A LISTAGEM DE NÚMEROS GERADOS 
# E TAMBÉM INDIQUE O MENOR E O MAIOR VALOR QUE ESTÃO NA TUPLA.

from random import randint
print('\n\033[34m====== DESAFIO 74 ======\n\033[m')

numeros = (randint(1,100),randint(1,100),randint(1,100),
           randint(1,100),randint(1,100))

print('Os valores sorteados foram: ', end='')
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior valor sorteado foi {max(numeros)}')
print(f'O menor valor sorteado foi {min(numeros)}')
