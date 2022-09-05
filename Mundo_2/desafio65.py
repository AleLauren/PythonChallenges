# DESAFIO 065
# CRIE UM PROGRAMA QUE LEIA VÁRIOS NÚMEROS INTEIROS PELO TECLADO. 
# NO FINAL DA EXECUÇÃO, MOSTRE A MÉDIA ENTRE TODOS OS VALORES 
# E QUAL FOI O MAIOR E O MENOR VALORES LIDOS. 
# O PROGRAMA DEVE PERGUNTAR AO USUÁRIO SE ELE QUER OU NÃO CONTINUAR A DIGITAR VALORES.

print('\n\033[34m====== DESAFIO 65 ======\n\033[m')

soma = cont = maior = menor = 0
resp = 'S'
while resp!= 'N':
    n = int(input('Digite um número: '))
    cont += 1
    soma += n
    if cont == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar? [S/N] ')).strip().upper()
print("""Você digitou {} números e a média entre eles foi {}
O maior valor foi {} e o menor foi {}""".format(cont,soma/cont,maior,menor))