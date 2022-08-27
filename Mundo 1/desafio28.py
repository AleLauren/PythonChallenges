# DESAFIO 028
# ESCREVA UM PROGRAMA QUE FAÇA O COMPUTADOR “PENSAR” EM UM NÚMERO INTEIRO 
# ENTRE 0 E 5 E PEÇA PARA O USUÁRIO TENTAR DESCOBRIR QUAL FOI O NÚMERO ESCOLHIDO PELO COMPUTADOR.
# O PROGRAMA DEVERÁ ESCREVER NA TELA SE O USUÁRIO VENCEU OU PERDEU.

from random import randint
from time import sleep
print('====== DESAFIO 28 ======')

print('-=-'*19)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-'*19)
num_user = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
num_pc = randint(0,5)
if num_pc == num_user:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print('GANHEI! Eu pensei no número {} e não no {}!'.format(num_pc,num_user))