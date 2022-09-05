# DESAFIO 051
# DESENVOLVA UM PROGRAMA QUE LEIA O PRIMEIRO TERMO E A RAZÃO DE UMA PA. 
# NO FINAL, MOSTRE OS 10 PRIMEIROS TERMOS DESSA PROGRESSÃO.

print('====== DESAFIO 51 ======')
print('='*24)
print('{:^24}'.format('10 TERMOS DE UMA PA'))
print('='*24)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
termos = str(n1)
for x in range(1,10):
    termos += " → " + str(n1+ x*r) 
print(termos + " → " + "ACABOU!")