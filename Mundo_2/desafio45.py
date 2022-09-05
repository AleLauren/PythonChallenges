# DESAFIO 045
# CRIE UM PROGRAMA QUE FAÇA O COMPUTADOR JOGAR JOKENPÔ COM VOCÊ.

from random import randint
from time import sleep
print('====== DESAFIO 45 ======')

print("""Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA""")

jogada_user = int(input('Qual é a sua jogada? '))

if jogada_user > 2:
    print('Jogada inválida. Tente novamente!')
else:
    jogada_pc = randint(0,2)
    sleep(0.5)
    print('JO')
    sleep(1)
    print('KEN')
    sleep(1)
    print('PO!!!')
    sleep(1)

    print('-='*12)
    itens = ('PEDRA', 'PAPEL', 'TESOURA')    
    print('Computador jogou {}'.format(itens[jogada_pc]))
    print('Jogador jogou {}'.format(itens[jogada_user]))
    print('-='*12)

# 0 ganha de 2 | 0 perde de 1
# 1 perde de 2 | 1 ganha de 0
# 2 perde de 0 | 2 ganha de 1

    if jogada_pc == jogada_user:
        resultado = 'EMPATOU! Tente novamente!'
    elif jogada_user == 0 and jogada_pc == 2:
        resultado = 'JOGADOR VENCE'
    elif jogada_user == 1 and jogada_pc == 0:
        resultado = 'JOGADOR VENCE'
    elif jogada_user == 2 and jogada_pc == 1:
        resultado = 'JOGADOR VENCE'
    else:
        resultado = 'JOGADOR PERDE'
    print('{}' .format(resultado))
