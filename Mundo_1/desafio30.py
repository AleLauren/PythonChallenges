# DESAFIO 030
# CRIE UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO 
# E MOSTRE NA TELA SE ELE É PAR OU ÍMPAR.

print('====== DESAFIO 30 ======')

n = int(input('Me diga um número qualquer: '))
if (n%2) == 0:
    print('O número {} é PAR'.format(n))
else:
    print('O número {} é ÍMPAR'.format(n))