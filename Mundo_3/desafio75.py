# DESAFIO 075
# DESENVOLVA UM PROGRAMA QUE LEIA QUATRO VALORES PELO TECLADO 
# E GUARDE-OS EM UMA TUPLA. NO FINAL, MOSTRE:
# A) QUANTAS VEZES APARECEU O VALOR 9.
# B) EM QUE POSIÇÃO FOI DIGITADO O PRIMEIRO VALOR 3.
# C) QUAIS FORAM OS NÚMEROS PARES.

print('\n\033[34m====== DESAFIO 75 ======\n\033[m')

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
n4 = int(input('Digite o último número: '))

numeros = (n1,n2,n3,n4)

print(f'Você digitou os valores: {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O valor 3 apareceu na {numeros.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado em nenhuma posição')
print('Os valores pares digitados foram ', end='')
for n in numeros:
    if n%2 ==0:
        print(n , end=' ' )
