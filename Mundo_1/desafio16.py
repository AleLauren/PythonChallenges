# DESAFIO 016
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO REAL QUALQUER PELO TECLADO
# E MOSTRE NA TELA A SUA PORÇÃO INTEIRA

from math import trunc
print('====== DESAFIO 16 ======')

numero = float(input('Digite um número real qualquer: '))
print('A parte inteira de {} é {}' .format(numero,trunc(numero)))

# é possível fazer apenas com a função interna int() 
# assim não precisa importa a biblioteca math