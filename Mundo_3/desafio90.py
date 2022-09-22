# DESAFIO 090
# FAÇA UM PROGRAMA QUE LEIA NOME E MÉDIA DE UM ALUNO, 
# GUARDANDO TAMBÉM A SITUAÇÃO EM UM DICIONÁRIO. 
# NO FINAL, MOSTRE O CONTEÚDO DA ESTRUTURA NA TELA.

print('\n\033[34m====== DESAFIO 90 ======\n\033[m')

aluno = {}

aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input('Média: '))

if aluno['Média'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Reprovado'

for k,v in aluno.items():
    print(f'  - {k} é igual a {v}')