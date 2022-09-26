# DESAFIO 099
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA MAIOR(), 
# QUE RECEBA VÁRIOS PARÂMETROS COM VALORES INTEIROS. 
# SEU PROGRAMA TEM QUE ANALISAR TODOS OS VALORES 
# E DIZER QUAL DELES É O MAIOR.    

from time import sleep

print('\n\033[34m====== DESAFIO 99 ======\n\033[m')

def maior(lst):
    maior = 0
    print('-='*30)
    print('Analisando os valores passados...')
    sleep(0.5)
    for p, n in enumerate(lst):
        if p == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        print(n, end=' ', flush=True)
        sleep(0.5)
    print(f'=> Foram informados {len(lst)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


while True:
    lista = []
    while True:
        lista.append(int(input('Digite um número para adicionar a lista: ')))
        while True:
            cont = str(input('Quer continuar? [S/N]')).upper().strip()[0]
            if cont in 'SN':
                break
            else: 
                print('Por favor digite apenas S ou N.')
        if cont == 'N':
            maior(lista)
            break
    while True:
        cont2 = str(input('Quer analisar outros números? [S/N]')).upper().strip()[0]
        if cont2 in 'SN':
            break
        else: 
            print('Valor inválido. Por favor digite S ou N.')
    if cont2 == 'N':
        break

# SOLUÇÃO COM DESEMPACOTAMENTO:
#def maior(* num): 
#   cont = maior = 0
#   for valor in num:
#       print(f'{valor} ', end='')   
#       if cont == 0:
#           maior = valor
#       else:
#           if valor > maior:
#               maior = valor
#       cont += 1 
