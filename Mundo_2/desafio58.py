# DESAFIO 058
# MELHORE O JOGO DO DESAFIO 28 ONDE O COMPUTADOR VAI “PENSAR” EM UM NÚMERO ENTRE 0 E 10. 
# SÓ QUE AGORA O JOGADOR VAI TENTAR ADIVINHAR ATÉ ACERTAR, 
# MOSTRANDO NO FINAL QUANTOS PALPITES FORAM NECESSÁRIOS PARA VENCER.

from random import randint
from time import sleep
print('\n\033[34m====== DESAFIO 58 ======\n\033[m')

print('-=-'*19)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-'*19)

num_user = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
num_pc = randint(0,10)

if num_pc == num_user:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    tent = 1
    while num_user != num_pc:
        if num_pc<num_user:
            print('Menos...Tente mais uma vez.')
        else:
            print('Mais...Tente mais uma vez.')
        num_user = int(input('Qual é seu palpite? '))
        tent += 1
    print('ACERTOU! Depois de {} tentativas...'.format(tent))