# DESAFIO 088
# FAÇA UM PROGRAMA QUE AJUDE UM JOGADOR DA MEGA SENA A CRIAR PALPITES.
# O PROGRAMA VAI PERGUNTAR QUANTOS JOGOS SERÃO GERADOS 
# E VAI SORTEAR 6 NÚMEROS ENTRE 1 E 60 PARA CADA JOGO, 
# CADASTRANDO TUDO EM UMA LISTA COMPOSTA.

from random import sample
from time import sleep
print('\n\033[34m====== DESAFIO 88 ======\n\033[m')

lista = []
print('-'*40)
print('{:^40}'.format('JOGA NA MEGA SENA'))
print('-'*40)

jogos = int(input('Quantos jogos você quer que eu sorteie? '))
print('='*10, f' SORTEANDO {jogos} JOGOS', '='*10)
sleep(1)
for j in range(0,jogos):
    lista.append(sample(range(1,60), 6))
    lista[j].sort()
    print(f'Jogo {j+1}: {lista[j]}')
    sleep(1)
print('{:=^40}'.format(' < BOA SORTE! > '))