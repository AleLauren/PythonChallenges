# DESAFIO 096
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ÁREA(), 
# QUE RECEBA AS DIMENSÕES DE UM TERRENO RETANGULAR (LARGURA E COMPRIMENTO) 
# E MOSTRE A ÁREA DO TERRENO.

print('\n\033[34m====== DESAFIO 96 ======\n\033[m')

def area(l,c):
    a = l*c
    print(f'A área de um terreno {l:.1f}x{c:.1f} é de {a:.1f}m².')


print('Controle de Terrenos')
print('-'*20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l,c)