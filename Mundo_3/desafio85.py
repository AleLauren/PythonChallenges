# DESAFIO 085
# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR SETE VALORES NUMÉRICOS 
# E CADASTRE-OS EM UMA LISTA ÚNICA QUE MANTENHA SEPARADOS OS VALORES PARES E ÍMPARES. 
# NO FINAL, MOSTRE OS VALORES PARES E ÍMPARES EM ORDEM CRESCENTE.

print('\n\033[34m====== DESAFIO 85 ======\n\033[m')

numeros = [[],[]]

for n in range(1,8):
    num = int(input(f'Digite o {n}º valor: '))
    if num % 2 == 0:
        numeros[0].append(num)
    else:
        numeros[1].append(num)
numeros[0].sort()
numeros[1].sort()
print(f'Os valores pares digitados foram : {numeros[0]}')
print(f'Os valores ímpares digitados foram : {numeros[1]}')
