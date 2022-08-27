# DESAFIO 035
# DESENVOLVA UM PROGRAMA QUE LEIA O COMPRIMENTO DE TRÊS RETAS 
# E DIGA AO USUÁRIO SE ELAS PODEM OU NÃO FORMAR UM TRIÂNGULO.

print('====== DESAFIO 35 ======')

print('-=-'*20)
print('{:^60}'.format('Analisador de Triângulos'))
print('-=-'*20)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

maior = l1
if l2 > l1 and l2 > l3:
    maior = l2
if l3 > l1 and l3 > l2:
    maior = l3

if maior < (l1 + l2 + l3) - maior:
    print('Os segmentos acima PODEM FORMAR triângulo!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')

# outra solução mais curta:
# if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
#    print('Os segmentos acima PODEM FORMAR triângulo!')
#else:
#    print('Os segmentos acima NÃO PODEM FORMAR triângulo')