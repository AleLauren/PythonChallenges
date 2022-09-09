# DESAFIO 080
# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR CINCO VALORES NUMÉRICOS 
# E CADASTRE-OS EM UMA LISTA, JÁ NA POSIÇÃO CORRETA DE INSERÇÃO (SEM USAR O SORT()). 
# NO FINAL, MOSTRE A LISTA ORDENADA NA TELA.

print('\n\033[34m====== DESAFIO 80 ======\n\033[m')

lista = []

for n in range (0,5):
    valor = int(input('Digite um valor: '))
    if n == 0 or valor > lista[-1]: 
        lista.append(valor)
        print('Adicionado ao final da lista...')
    else:
        for pos, x in enumerate(lista):
            if valor <= x:
                lista.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista...')
                break
            
# SOLUÇÃO COM WHILE
#        pos = 0
#        while pos < len(lista):
#            if valor <= lista[pos]:
#                lista.insert(pos, valor)
#                print(f'Adicionado na posição {pos} da lista...')
#                break
#            pos +=1

print('-='*30)
print(f'Os valores digitados em ordem foram {lista}')
