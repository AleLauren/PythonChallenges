# DESAFIO 100
# FAÇA UM PROGRAMA QUE TENHA UMA LISTA CHAMADA NÚMEROS 
# E DUAS FUNÇÕES CHAMADAS SORTEIA() E SOMAPAR(). 
# A PRIMEIRA FUNÇÃO VAI SORTEAR 5 NÚMEROS E VAI COLOCÁ-LOS 
# DENTRO DA LISTA E A SEGUNDA FUNÇÃO VAI MOSTRAR 
# A SOMA ENTRE TODOS OS VALORES PARES SORTEADOS PELA FUNÇÃO ANTERIOR.        

from random import randint
from time import sleep

print('\n\033[34m====== DESAFIO 100 ======\n\033[m')

def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    sleep(0.5)
    for cont in range(0,5):
        n = randint(1, 10)
        lista.append(n)
        print(n, end=' ', flush=True)
        sleep(0.5)
    print('PRONTO!')


def somaPar(lista):
    soma = 0
    for n in lista:
        if n % 2 == 0:
            soma +=n
    print(f'Somando os valores pares de {lista}, temos {soma}')


números = []
sorteia(números)
somaPar(números)

