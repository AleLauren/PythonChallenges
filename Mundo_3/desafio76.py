# DESAFIO 076
# CRIE UM PROGRAMA QUE TENHA UMA TUPLA ÚNICA 
# COM NOMES DE PRODUTOS E SEUS RESPECTIVOS PREÇOS, NA SEQUÊNCIA. 
# NO FINAL, MOSTRE UMA LISTAGEM DE PREÇOS, ORGANIZANDO OS DADOS EM FORMA TABULAR.

print('\n\033[34m====== DESAFIO 76 ======\n\033[m')

listagem = ('Pão', 1, 'Leite', 3.5, 'Frango', 10.90)

print('-'*60)
print('{:^60}' .format('LISTAGEM DE PREÇOS'))
print('-'*60)
for n in range(0,len(listagem)):
    if n%2==0:
        print('{:.<51}R${:>7.2f}'.format(listagem[n],listagem[n+1]))
print('_'*60)
