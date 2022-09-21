# DESAFIO 089
# CRIE UM PROGRAMA QUE LEIA NOME E DUAS NOTAS DE VÁRIOS ALUNOS E GUARDE TUDO EM UMA LISTA COMPOSTA. 
# NO FINAL, MOSTRE UM BOLETIM CONTENDO A MÉDIA DE CADA UM 
# E PERMITA QUE O USUÁRIO POSSA MOSTRAR AS NOTAS DE CADA ALUNO INDIVIDUALMENTE.

print('\n\033[34m====== DESAFIO 89 ======\n\033[m')

boletim_turma = []

while True:
    aluno = [[],[]]
    aluno[0].append(str(input('Nome: ')).strip())
    aluno[1].append(float(input('Nota 1: ')))
    aluno[1].append(float(input('Nota 2: ')))
    boletim_turma.append(aluno[:])
    aluno.clear()
    cont = input('Quer continuar? [S/N] ').strip()[0]
    if cont in 'Nn':
        break
print('-='*20)
print(f'{"No.":<5}{"NOME":<28}{"MÉDIA":>5}')
print('-'*40)
for n in range(0,len(boletim_turma)):
    print('{:<5}'.format(n), end='')
    print('{:<28}'.format(boletim_turma[n][0][0]), end='')
    media = (boletim_turma[n][1][0] + boletim_turma[n][1][1]) / 2
    print('{:>5.1f}'.format(media))
print('-'*40)
while True:
    id_aluno = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    if id_aluno in range(0,len(boletim_turma)):
        print(f'Notas de {boletim_turma[id_aluno][0][0]} são {boletim_turma[id_aluno][1]}')
        print('-'*40)
    elif id_aluno == 999:
        print('FINALIZANDO...')
        print('<<< VOLTE SEMPRE >>>')
        break
    else:
        print('Nº de aluno inválido. Tente novamente.')