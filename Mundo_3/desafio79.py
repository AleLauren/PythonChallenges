# DESAFIO 079
# CRIE UM PROGRAMA ONDE O USUÁRIO POSSA DIGITAR VÁRIOS VALORES NUMÉRICOS 
# E CADASTRE-OS EM UMA LISTA. CASO O NÚMERO JÁ EXISTA LÁ DENTRO, 
# ELE NÃO SERÁ ADICIONADO. NO FINAL, SERÃO EXIBIDOS 
# TODOS OS VALORES ÚNICOS DIGITADOS, EM ORDEM CRESCENTE.

print('\n\033[34m====== DESAFIO 79 ======\n\033[m')

valores = []
while True:
    n = int(input(f'Digite um valor: '))
    if n in valores:
        print('Valor duplicado! Não vou adicionar...')
    else:
        valores.append(n)
        print('Valor adicionado com sucesso...')
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
valores.sort()
print(f'Você digitou os valores {valores}')
