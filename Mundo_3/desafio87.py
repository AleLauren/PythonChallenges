# DESAFIO 087
# APRIMORE O DESAFIO ANTERIOR, MOSTRANDO NO FINAL:                                                    
# A) A SOMA DE TODOS OS VALORES PARES DIGITADOS.
# B) A SOMA DOS VALORES DA TERCEIRA COLUNA.
# C) O MAIOR VALOR DA SEGUNDA LINHA.

print('\n\033[34m====== DESAFIO 87 ======\n\033[m')

numeros = [[],[],[]]
soma_pares = soma_3c = maior_2l = 0

for l in range(0,3):
    for c in range(0,3):
        numeros[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-='*30)
for l in range(0,3):
    for c in range(0,3): 
        print(f'[{numeros[l][c]:^5}]', end=' ')
        if numeros[l][c] % 2 == 0:
            soma_pares += numeros[l][c]
        if c == 2:
            soma_3c += numeros[l][c]
        if l == 1: 
            if numeros[l][c] > maior_2l:
                maior_2l = numeros[l][c]
    print('')
print('-='*30)

print(f'A soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_3c}')
print(f'O maior valor da segunda linha é {maior_2l}')
