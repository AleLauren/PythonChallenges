# DESAFIO 064
# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. 
# O PROGRAMA SÓ VAI PARAR QUANDO O USUÁRIO DIGITAR O VALOR 999, QUE É A CONDIÇÃO DE PARADA. 
# NO FINAL, MOSTRE QUANTOS NÚMEROS FORAM DIGITADOS 
# E QUAL FOI A SOMA ENTRE ELES (DESCONSIDERANDO O FLAG).

print('\n\033[34m====== DESAFIO 64 ======\n\033[m')

cont = soma = n = 0
n = int(input('Digite um número [999 para parar]: '))
while n!=999:
    cont += 1
    soma += n
    n = int(input('Digite um número [999 para parar]: '))
print('Você digitou {} números e a soma entre eles foi {}.'.format(cont,soma))