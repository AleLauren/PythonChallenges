# DESAFIO 009
# FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO QUALQUER 
# E MOSTRE NA TELA SUA TABUADA.

print('====== DESAFIO 09 ======')
x=int(input('Digite um número pra ver sua tabuada: '))
print('===== TABUADA DE {} ====='.format(x))
print('='*24)

#solução 01
#print('{} x  1 = {} \n{} x  2 = {} \n{} x  3 = {} \n{} x  4 = {} \n{} x  5 = {}'.format(x,x*1,x,x*2,x,x*3,x,x*4,x,x*5))
#print('{} x  6 = {} \n{} x  7 = {} \n{} x  8 = {} \n{} x  9 = {} \n{} x 10 = {}'.format(x,x*6,x,x*7,x,x*8,x,x*9,x,x*10))

#solução 02
#print('{} x {:2} = {}'.format(x,1,x*1))
#print('{} x {:2} = {}'.format(x,2,x*2))
#print('{} x {:2} = {}'.format(x,3,x*3))
#print('{} x {:2} = {}'.format(x,4,x*4))
#print('{} x {:2} = {}'.format(x,5,x*5))
#print('{} x {:2} = {}'.format(x,6,x*6))
#print('{} x {:2} = {}'.format(x,7,x*7))
#print('{} x {:2} = {}'.format(x,8,x*8))
#print('{} x {:2} = {}'.format(x,9,x*9))
#print('{} x {:2} = {}'.format(x,10,x*10))

#solução mais avançada usando "for"
numbers=(range(1,11))
for y in numbers:
    print('{} x {:2} = {}'.format(x,y,x*y))
print('='*24)