# DESAFIO 042
# REFAÇA O DESAFIO 35 DOS TRIÂNGULOS, ACRESCENTANDO O RECURSO DE 
# MOSTRAR QUE TIPO DE TRIÂNGULO SERÁ FORMADO:
#– EQUILÁTERO: TODOS OS LADOS IGUAIS
#– ISÓSCELES: DOIS LADOS IGUAIS, UM DIFERENTE
#– ESCALENO: TODOS OS LADOS DIFERENTES

print('====== DESAFIO 42 ======')

print('-=-'*20)
print('{:^60}'.format('Analisador de Triângulos'))
print('-=-'*20)

l1 = float(input('Primeiro segmento: '))
l2 = float(input('Segundo segmento: '))
l3 = float(input('Terceiro segmento: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l2 + l1:
    if l1 == l2 == l3:
        print('Os segmentos acima PODEM FORMAR um triângulo EQUILÁTERO!')
    elif l1 != l2 != l3 != l1:
        print('Os segmentos acima PODEM FORMAR um triângulo ESCALENO!') 
    else:
        print('Os segmentos acima PODEM FORMAR um triângulo ISÓSCELES!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR triângulo')