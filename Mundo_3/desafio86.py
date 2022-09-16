# DESAFIO 086
# CRIE UM PROGRAMA QUE DECLARE UMA MATRIZ DE DIMENSÃO 3×3 
# E PREENCHA COM VALORES LIDOS PELO TECLADO. 
# NO FINAL, MOSTRE A MATRIZ NA TELA, COM A FORMATAÇÃO CORRETA.

print('\n\033[34m====== DESAFIO 86 ======\n\033[m')

numeros = [[],[],[]]
for l in range(0,3):
    for c in range(0,3):
        numeros[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
print('-='*30)
for l in range(0,3):
    for c in range(0,3): 
        print(f'[{numeros[l][c]:^5}]', end=' ')
    print('')
