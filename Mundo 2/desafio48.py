# DESAFIO 048
# FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OS NÚMEROS 
# QUE SÃO MÚLTIPLOS DE TRÊS E QUE SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.

print('====== DESAFIO 48 ======')

contador = 0
soma = 0
for n in range(3,500,3):
    if n % 2 != 0:
        contador += 1
        soma += n
        
print('A soma de todos os {} valores solicitados é {}' .format(contador, soma))