# DESAFIO 037
# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER 
# E PEÇA PARA O USUÁRIO ESCOLHER QUAL SERÁ A BASE DE CONVERSÃO: 
# 1 PARA BINÁRIO, 2 PARA OCTAL E 3 PARA HEXADECIMAL.

print('====== DESAFIO 37 ======')

n = int(input('Digite um número inteiro: '))
opcao = int(input("""Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: """))

# -----------------------------------------------------------------------------------

# SOLUÇÃO SIMPLIFICADA USANDO O CONVERSOR DO PYTHON:

#if opcao == 1:
#    print('{} convertido para BINÁRIO é igual a {}'.format(n, bin(n)[2:]))
#elif opcao == 2:
#    print('{} convertido para OCTAL é igual a {}'.format(n, oct(n)[2:]))   
#elif opcao == 3:
#    print('{} convertido para HEXADECIMAL é igual a {}'.format(n, hex(n)[2:]))
#else:
#    print('Opção inválida. Tente novamente.')

# -----------------------------------------------------------------------------------

# SOLUÇÃO CRIANDO NOSSO PRÓPRIO CONVERSOR PARA BINÁRIO / OCTAL / HEXADECIMAL: 
# Para isso, temos que fazer sucessivas divisões por 2 / 8 / 16 
# até que o valor da divisão inteira seja zero.
# O número convertido é a junção de todos os restos das divisões
# do último resto, até o primeiro

# vamos usar a variável nb para fazer as divisões 
nb = n

# Se opção for um número diferente de 1, 2 ou 3: 
if opcao != 1 and opcao != 2 and opcao != 3:
    print('Opção inválida. Tente novamente')
# Opção selecionada é um número válido: 
else:
    if opcao == 1:
        d=2
        base = 'BINÁRIO'
    elif opcao == 2:
        d=8
        base = 'OCTAL'
    elif opcao == 3:
        d=16
        base = 'HEXADECIMAL'

# A base hexadecimal usa letras, então precisamos definir as exceções

    if nb%d == 10:
        num_convertido = str('A')
    elif nb%d == 11:
        num_convertido = str('B')
    elif nb%d == 12:
        num_convertido = str('C')
    elif nb%d == 13:
        num_convertido = str('D')
    elif nb%d == 14:
        num_convertido = str('E')
    elif nb%d == 15:
        num_convertido = str('F')
    else:
        num_convertido = str(nb%d)

    while nb // d != 0:
        nb = nb // d
        if nb%d == 10:
            num_convertido = num_convertido + str('A')
        elif nb%d == 11:
            num_convertido = num_convertido + str('B')
        elif nb%d == 12:
            num_convertido = num_convertido + str('C')
        elif nb%d == 13:
            num_convertido = num_convertido + str('D')
        elif nb%d == 14:
            num_convertido = num_convertido + str('E')
        elif nb%d == 15:
            num_convertido = num_convertido + str('F')
        else:
            num_convertido = num_convertido + str(nb%d)

    print('{} convertido para {} é igual a {} '.format(n,base,num_convertido[::-1]))