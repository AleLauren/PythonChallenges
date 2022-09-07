# DESAFIO 067
# FAÇA UM PROGRAMA QUE MOSTRE A TABUADA DE VÁRIOS NÚMEROS, UM DE CADA VEZ, 
# PARA CADA VALOR DIGITADO PELO USUÁRIO. 
# O PROGRAMA SERÁ INTERROMPIDO QUANDO O NÚMERO SOLICITADO FOR NEGATIVO.

print('\n\033[34m====== DESAFIO 67 ======\n\033[m')

while True:
    n=int(input('Digite um número pra ver sua tabuada: '))
    if n < 0:
        break
    print(f'===== TABUADA DE {n} =====')
    print('='*24)
    for x in range(1,11):
        print(f'{n} x {x:2} = {n*x}')
    print('='*24)
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')