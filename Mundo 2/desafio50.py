# DESAFIO 050
# DESENVOLVA UM PROGRAMA QUE LEIA SEIS NÚMEROS INTEIROS 
# E MOSTRE A SOMA APENAS DAQUELES QUE FOREM PARES. 
# SE O VALOR DIGITADO FOR ÍMPAR, DESCONSIDERE-O. 

print('====== DESAFIO 50 ======')

soma = 0
cont = 0 
lista = ['primeiro', 'segundo', 'terceiro', 'quarto', 'quinto', 'sexto']
for n in lista:
    x = int(input('Digite o {} número inteiro: ' .format(n)))
    if x % 2 == 0:
        soma += x
        cont += 1
print('Você informou {} números PARES e a soma foi {}'.format(cont,soma))