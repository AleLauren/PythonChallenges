# DESAFIO 091
# CRIE UM PROGRAMA ONDE 4 JOGADORES JOGUEM UM DADO E
# TENHAM RESULTADOS ALEATÓRIOS. GUARDE ESSES RESULTADOS EM UM DICIONÁRIO EM PYTHON. 
# NO FINAL, COLOQUE ESSE DICIONÁRIO EM ORDEM, SABENDO QUE O VENCEDOR TIROU O MAIOR NÚMERO NO DADO.

from random import randint
from time import sleep
from operator import itemgetter

print('\n\033[34m====== DESAFIO 91 ======\n\033[m')

jogo = {}
ranking =[]

print(' VAMOS JOGAR OS DADOS! ')
print('='*30)
sleep(0.5)
print('- Valores sorteados: ')
sleep(0.5)
for n in range(0,4):
    jogo[f'Jogador {n+1}'] = randint(1, 6)
for k,v in jogo.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('='*30)
print('- Ranking dos jogadores: ')

ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º lugar: {v[0]} com {v[1]}')
    sleep(1)