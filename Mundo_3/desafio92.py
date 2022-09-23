# DESAFIO 092
# CRIE UM PROGRAMA QUE LEIA NOME, ANO DE NASCIMENTO 
# E CARTEIRA DE TRABALHO E CADASTRE-O (COM IDADE) EM UM DICIONÁRIO. 
# SE POR ACASO A CTPS FOR DIFERENTE DE ZERO, 
# O DICIONÁRIO RECEBERÁ TAMBÉM O ANO DE CONTRATAÇÃO E O SALÁRIO. 
# CALCULE E ACRESCENTE, ALÉM DA IDADE, COM QUANTOS ANOS A PESSOA VAI SE APOSENTAR.

from datetime import date

print('\n\033[34m====== DESAFIO 92 ======\n\033[m')

cadastro = {}

cadastro['Nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de Nascimento: '))
cadastro['Idade'] = date.today().year - ano_nascimento
cadastro['CTPS'] = int(input('Carteira de Trabalho (0 não tem): '))
if cadastro['CTPS'] != 0: 
    cadastro['Contratação'] = int(input('Ano de Contratação: '))
    cadastro['Salário'] = int(input('Salário: R$ '))
    ano_aposentadoria = cadastro['Contratação'] + 35 
    cadastro['Aposentadoria'] = ano_aposentadoria - ano_nascimento
print('='*30)
for k,v in cadastro.items():
    print(f' - {k} tem o valor {v}')