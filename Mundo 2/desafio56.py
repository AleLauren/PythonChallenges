# DESAFIO 056
# DESENVOLVA UM PROGRAMA QUE LEIA O NOME, IDADE E SEXO DE 4 PESSOAS. 
# NO FINAL DO PROGRAMA, MOSTRE: A MÉDIA DE IDADE DO GRUPO, 
# QUAL É O NOME DO HOMEM MAIS VELHO E QUANTAS MULHERES TÊM MENOS DE 20 ANOS.

print('\033[34m====== DESAFIO 56 ======\n\033[m')

soma_idade = 0
idade_velho = 0
nome_velho = 0
f_sub20 = 0

for n in range(1,5):
    print('======= {}ª PESSOA ======='.format(n))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    soma_idade += idade
    if sexo == 'F' and idade < 20:
        f_sub20 += 1
    if sexo == 'M' and idade > idade_velho:
        idade_velho = idade
        nome_velho = nome

print('A média de idade do grupo é de {:.1f} anos.' .format(soma_idade/4))
print('O homem mais velho tem {} anos e se chama {}.' .format(idade_velho, nome_velho))
print('Ao todo são {} mulheres com menos de 20 anos.' .format(f_sub20))

