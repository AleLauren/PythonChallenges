# DESAFIO 052
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO 
# E DIGA SE ELE É OU NÃO UM NÚMERO PRIMO. 

print('====== DESAFIO 52 ======')

p = int(input('Digite um número: '))
cont = 0

for c in range(1,p+1):
    if p % c == 0:
        cont += 1
        print('\033[31m', end='')
    else:
        print('\033[34m', end='')
    print('{}' .format(c) , end=' ')

print('\n\033[mO número {} foi dividido {} vezes' .format(p, cont))
if cont == 2:
    print('Por isso ele é PRIMO')
else:
    print('Por isso ele NÃO é PRIMO')
 