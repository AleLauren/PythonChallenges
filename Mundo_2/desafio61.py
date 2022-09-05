# DESAFIO 061
# REFAÇA O DESAFIO 51, LENDO O PRIMEIRO TERMO E A RAZÃO DE UMA PA, 
# MOSTRANDO OS 10 PRIMEIROS TERMOS DA PROGRESSÃO USANDO A ESTRUTURA WHILE.

print('\n\033[34m====== DESAFIO 61 ======\n\033[m')

print('='*24)
print('{:^24}'.format('10 TERMOS DE UMA PA'))
print('='*24)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
x = 0
while x < 10:
    termos = n1 + x*r
    print("{} → ".format(termos) , end="")
    x += 1
print('ACABOU!')