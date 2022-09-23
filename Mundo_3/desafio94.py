# DESAFIO 094
# CRIE UM PROGRAMA QUE LEIA NOME, SEXO E IDADE DE VÁRIAS PESSOAS, GUARDANDO OS DADOS 
# DE CADA PESSOA EM UM DICIONÁRIO E TODOS OS DICIONÁRIOS EM UMA LISTA. NO FINAL, MOSTRE: 
# A) QUANTAS PESSOAS FORAM CADASTRADAS 
# B) A MÉDIA DE IDADE 
# C) UMA LISTA COM AS MULHERES 
# D) UMA LISTA DE PESSOAS COM IDADE ACIMA DA MÉDIA

print('\n\033[34m====== DESAFIO 94 ======\n\033[m')

cadastro = []
pessoa ={}
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    cadastro.append(pessoa.copy())
    while True:
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Por favor, digite apenas S ou N.')
    if cont == 'N':
        break
print('-='*30)
print(f'- O grupo tem {len(cadastro)} pessoas')
print(f'- A média de idade é de {soma/len(cadastro):.2f} anos.')
print('- As mulheres cadastradas foram: ', end='')
for n in range(0,len(cadastro)):
    if cadastro[n]['sexo'] in 'Ff':
        print(cadastro[n]['nome'] , end='  ')
print()
print('- Lista das pessoas que estão acima da média: ')
for n in range(0,len(cadastro)):
    if cadastro[n]['idade'] > (soma/len(cadastro)):
        for k, v in pessoa.items():
            print(f'{k} = {v}; ', end='')
        print()
print('<< ENCERRADO >>')
