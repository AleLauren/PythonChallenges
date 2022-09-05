# DESAFIO 006
# CRIE UM ALGORITMO QUE LEIA UM NÚMERO E
# MOSTRE O SEU DOBRO, TRIPLO E RAIZ QUADRADA.

print('====== DESAFIO 06 ======')
n = int(input('Digite um número: '))
print('O dobro de {} é {} e o triplo é {}.'.format(n, n*2, n*3))
print('A raiz quadrada de {} é {:.2f}.'.format(n, float(n**(1/2))))