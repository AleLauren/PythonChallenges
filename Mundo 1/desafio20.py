# DESAFIO 020
# O MESMO PROFESSOR DO DESAFIO 19 QUER SORTEAR A ORDEM DE APRESENTAÇÃO DE TRABALHOS DOS ALUNOS. 
# FAÇA UM PROGRAMA QUE LEIA O NOME DOS QUATRO ALUNOS E MOSTRE A ORDEM SORTEADA.

import random
print('====== DESAFIO 20 ======')

p1 = input('Primeiro aluno: ')
p2 = input('Segundo aluno: ')
p3 = input('Terceiro aluno: ')
p4 = input('Quarto aluno: ')
lista = [p1, p2, p3, p4]
random.shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))