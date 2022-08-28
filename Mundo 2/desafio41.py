# DESAFIO 041
# A CONFEDERAÇÃO NACIONAL DE NATAÇÃO PRECISA DE UM PROGRAMA 
# QUE LEIA O ANO DE NASCIMENTO DE UM ATLETA 
# E MOSTRE SUA CATEGORIA, DE ACORDO COM A IDADE:
#– ATÉ 9 ANOS: MIRIM
#– ATÉ 14 ANOS: INFANTIL
#– ATÉ 19 ANOS: JÚNIOR
#– ATÉ 25 ANOS: SÊNIOR
#– ACIMA DE 25 ANOS: MASTER

from datetime import date
print('====== DESAFIO 41 ======')

nasc = int(input('Ano de Nascimento: '))
ano = date.today().year
idade = ano - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM')
elif idade <= 14:
    print('Classificação: INFANTIL')
elif idade <= 19:
    print('Classificação: JÚNIOR')    
elif idade <= 25:
    print('Classificação: SÊNIOR')
else:    
    print('Classificação: MASTER') 