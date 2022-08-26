# DESAFIO 022
# CRIE UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA E MOSTRE:
# – O NOME COM TODAS AS LETRAS MAIÚSCULAS E MINÚSCULAS.
# – QUANTAS LETRAS TEM NO TOTAL (SEM CONSIDERAR ESPAÇOS).
# – QUANTAS LETRAS TEM O PRIMEIRO NOME.

print('====== DESAFIO 22 ======')

nome_completo = str(input('Digite seu nome completo: ')).strip()
# strip remove os espaços antes e depois
print('Seu nome em maiúsculas é {}.'.format(nome_completo.upper()))
print('Seu nome em minúsculas é {}.'.format(nome_completo.lower()))
c=int(len(nome_completo))
e=int(nome_completo.count(' '))
print('Seu nome tem ao todo {} letras.'.format(c-e))
nomes=nome_completo.split()
print('Seu primeiro nome é {} e ele tem {} letras.'.format(nomes[0],len(nomes[0])))