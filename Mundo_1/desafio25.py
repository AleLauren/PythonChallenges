# DESAFIO 025
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA PESSOA 
# E DIGA SE ELA TEM “SILVA” NO NOME.

print('====== DESAFIO 25 ======')

nome = str(input('Qual é seu nome completo: ')).strip()
print("Seu nome tem Silva? {}" .format('silva' in nome.lower()))
