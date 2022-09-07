# DESAFIO 068
# FAÇA UM PROGRAMA QUE JOGUE PAR OU ÍMPAR COM O COMPUTADOR. 
# O JOGO SÓ SERÁ INTERROMPIDO QUANDO O JOGADOR PERDER, 
# MOSTRANDO O TOTAL DE VITÓRIAS CONSECUTIVAS QUE ELE CONQUISTOU NO FINAL DO JOGO.

from random import randint
print('\n\033[34m====== DESAFIO 68 ======\n\033[m')

v = 0
print('=-'*24)
print('VAMOS JOGAR PAR OU ÍMPAR')

while True:
    print('=-'*24)
    n = int(input('Diga um valor: '))
    n_pc = randint(0, 11)
    p_i = ' '
# valida se o tipo é par ou ímpar
    while p_i not in 'PpIi':
# o zero ao final indica que só a primeira letra será considerada
        p_i = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    if (n+n_pc) % 2 == 0:
        r = 'P'
    else:
        r = 'I'
    print('-'*48)
    print(f'Você jogou {n} e o computador {n_pc}. Total de {n+n_pc}. ' , end='')
    print('DEU PAR' if r == 'P' else 'DEU ÍMPAR')
    print('-'*48)
    if r == p_i:
        print("""Você GANHOU!
Vamos jogar novamente...""")
        v += 1
    else:
        print('Você PERDEU!')
        break
    
print('=-'*24)
print(f'GAME OVER! Você venceu {v} vezes.')
