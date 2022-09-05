# DESAFIO 033
# FAÇA UM PROGRAMA QUE LEIA TRÊS NÚMEROS 
# E MOSTRE QUAL É O MAIOR E QUAL É O MENOR.

print('====== DESAFIO 33 ======')
v1=int(input('Primeiro valor: '))
v2=int(input('Segundo valor: '))
v3=int(input('Terceiro valor: '))

menor = v1
if v2 < v1 and v2 < v3:
    menor = v2
if v3 < v1 and v3 < v2:
    menor = v3

maior = v1 
if v2 > v1 and v2 > v3:
    maior = v2
if v3 > v1 and v3 > v2:
    maior = v3

print('O menor valor digitado foi {}' .format(menor))
print('O maior valor digitado foi {}' .format(maior))