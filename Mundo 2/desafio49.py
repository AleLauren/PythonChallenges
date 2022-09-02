# DESAFIO 049
# REFAÇA O DESAFIO 9, MOSTRANDO A TABUADA DE UM NÚMERO 
# QUE O USUÁRIO ESCOLHER, SÓ QUE AGORA UTILIZANDO UM LAÇO FOR. 

print('====== DESAFIO 49 ======')

x=int(input('Digite um número pra ver sua tabuada: '))
print('===== TABUADA DE {} ====='.format(x))
print('='*24)
num =(range(1,11))
for y in num:
    print('{} x {:2} = {}'.format(x,y,x*y))
print('='*24)