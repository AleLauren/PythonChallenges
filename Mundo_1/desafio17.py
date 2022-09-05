# DESAFIO 017
# FAÇA UM PROGRAMA QUE LEIA O COMPRIMENTO DO CATETO OPOSTO
# E DO CATETO ADJACENTE DE UM TRIÂNGULO RETÂNGULO,
# CALCULE E MOSTRE O COMPRIMENTO DA HIPOTENUSA

from math import sqrt
print('====== DESAFIO 17 ======')

print('Vamos calcular a hipotenusa de um triângulo retângulo!')
o = float(input('Digite o comprimento do cateto oposto: '))
a = float(input('E do cateto adjacente: '))
h = sqrt(o**2 + a**2)
# h = (o**2 + a**2) ** (1/2)
# h = math.hypot(o,a)
print('O valor da hipotenusa é {:.2f}' .format(h))