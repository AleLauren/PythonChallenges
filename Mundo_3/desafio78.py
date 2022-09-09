# DESAFIO 078
# FAÇA UM PROGRAMA QUE LEIA 5 VALORES NUMÉRICOS E GUARDE-OS EM UMA LISTA. 
# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR VALOR DIGITADO 
# E AS SUAS RESPECTIVAS POSIÇÕES NA LISTA.

print('\n\033[34m====== DESAFIO 78 ======\n\033[m')

valores = []
for n in range (0,5):
    valores.append(int(input(f'Digite um valor para a posição {n}: ')))
print('-='*30)
print(f'Você digitou os valores {valores}')
print(f'O maior valor digitado foi {max(valores)} nas posições ', end='')
for c,v in enumerate(valores):
    if v == max(valores):
        print(f'{c} ... ', end='')
print(f'\nO menor valor digitado foi {min(valores)} nas posições ', end='')
for c,v in enumerate(valores):
    if v == min(valores):
        print(f'{c} ...', end='')