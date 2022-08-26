# DESAFIO 019
# UM PROFESSOR QUER SORTEAR UM DOS SEUS QUATRO ALUNOS PARA APAGAR O QUADRO. 
# FAÇA UM PROGRAMA QUE AJUDE ELE, LENDO O NOME DOS ALUNOS 
# E ESCREVENDO NA TELA O NOME DO ESCOLHIDO.

import random
print('====== DESAFIO 19 ======')

p1 = input('Primeiro aluno: ')
p2 = input('Segundo aluno: ')
p3 = input('Terceiro aluno: ')
p4 = input('Quarto aluno: ')
lista = [p1, p2, p3, p4]
print('O aluno escolhido foi: {}'.format(random.choice(lista)))

