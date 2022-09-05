# DESAFIO 023
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO DE 0 A 9999 
# E MOSTRE NA TELA CADA UM DOS DÍGITOS SEPARADOS.

print('====== DESAFIO 23 ======')

num = int(input('Informe um número: '))
print('Analisando o número {}'.format(num))
# "//" é a divisão inteira e "%" é o resto da divisão
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Unidade : {}'.format(u))
print('Dezena : {}'.format(d))
print('Centena : {}'.format(c))
print('Milhar : {}'.format(m))