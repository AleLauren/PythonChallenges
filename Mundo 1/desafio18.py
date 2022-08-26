# DESAFIO 018
# FAÇA UM PROGRAMA QUE LEIA UM ÂNGULO QUALQUER 
# E MOSTRE NA TELA O VALOR DO SENO, COSSENO 
# E TANGENTE DESSE ÂNGULO.

import math
print('====== DESAFIO 18 ======')

a = float(input('Digite o valor do ângulo: '))
# temos que converter de graus para radianos
x = math.radians(a)
print('Para o ângulo de {} graus, o seno é {:.2f}, o cosseno é {:.2f} e a tangente é {:.2f}.' .format(a,math.sin(x),math.cos(x),math.tan(x)))
