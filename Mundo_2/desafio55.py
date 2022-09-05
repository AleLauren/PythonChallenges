# DESAFIO 055
# FAÇA UM PROGRAMA QUE LEIA O PESO DE CINCO PESSOAS. 
# NO FINAL, MOSTRE QUAL FOI O MAIOR E O MENOR PESO LIDOS.

print('\033[34m====== DESAFIO 55 ======\n\033[m')

peso_1 = float((input('Digite o peso da 1ª pessoa: ')))
maior = peso_1
menor = peso_1

for n in range(2,6):
    peso = float(input('Digite o peso da {}ª pessoa: '.format(n)))
    if peso > maior:
        maior = peso
    if peso < menor:
        menor = peso

print('O maior peso é de {:.2f}kg e o menor peso é de {:.2f}kg.'.format(maior, menor))

# É possível definir maior e menor = 0 no começo
# e adicionar um if n == 1 : maior = peso / menor = peso
# e colocar as condições de > e < dentro de um else
