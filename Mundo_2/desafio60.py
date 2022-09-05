# DESAFIO 060
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO QUALQUER E MOSTRE O SEU FATORIAL.

print('\n\033[34m====== DESAFIO 60 ======\n\033[m')

n = int(input('Digite um número para calcular seu fatorial: '))
print('Calculando {}! = '.format(n), end='')
if n == 1:
    print('1')
else:
    n_fat = 1
    while n != 0:
        print('{}' .format(n), end='')
        print(' x ' if n > 1 else ' = {}'.format(n_fat), end='')
        n_fat *= n
        n -= 1

# solução mais simples usando função
#from math import factorial
#num = int(input('Digite um número para calcular seu fatorial: '))
#print('O fatorial de {}! é {}'.format(num,factorial(num)))

# solução usando for
#n = int(input('Digite um número para calcular seu fatorial: '))
#print('Calculando {}! = '.format(n), end='')
#n_fat = 1
#for p in range(n,1,-1):
#    print(p , end=" x ")
#    n_fat *= p
#if n == 1:
#    print(' 1')
#else:
#    print('1 = {}'.format(n_fat))