# DESAFIO 081
# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA.                  
# DEPOIS DISSO, MOSTRE:
# A) QUANTOS NÚMEROS FORAM DIGITADOS.
# B) A LISTA DE VALORES, ORDENADA DE FORMA DECRESCENTE.
# C) SE O VALOR 5 FOI DIGITADO E ESTÁ OU NÃO NA LISTA.

print('\n\033[34m====== DESAFIO 81 ======\n\033[m')

valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break 
print('-='*30)
print(f'Você digitou {len(valores)} elementos.')
valores.sort(reverse=True)
print(f'Os valores em ordem decrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')