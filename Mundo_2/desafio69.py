# DESAFIO 069
# CRIE UM PROGRAMA QUE LEIA A IDADE E O SEXO DE VÁRIAS PESSOAS. 
# A CADA PESSOA CADASTRADA, O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO QUER OU NÃO CONTINUAR. 
# NO FINAL, MOSTRE:
# A) QUANTAS PESSOAS TEM MAIS DE 18 ANOS.
# B) QUANTOS HOMENS FORAM CADASTRADOS.
# C) QUANTAS MULHERES TEM MENOS DE 20 ANOS.

print('\n\033[34m====== DESAFIO 69 ======\n\033[m')

adultos = homens = mulher_sub20 = 0

while True:
    sexo = continuar = ' '
    print('-'*21)
    print(' CADASTRE UMA PESSOA')
    print('-'*21)
    idade = int(input('Idade: '))
    while sexo not in 'MF':
        sexo = str(input('Sexo: [M/F] ')).strip().upper()[0]
    print('-'*21)
    if idade >= 18:
        adultos += 1
    if idade < 20 and sexo == 'F':
        mulher_sub20 += 1
    if sexo == 'M':
        homens += 1
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('FIM DO PROGRAMA')
print(f'Total de pessoas com mais de 18 anos: {adultos}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher_sub20} mulheres com menos de 20 anos')