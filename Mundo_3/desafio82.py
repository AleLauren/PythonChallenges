# DESAFIO 082
# CRIE UM PROGRAMA QUE VAI LER VÁRIOS NÚMEROS E COLOCAR EM UMA LISTA. 
# DEPOIS DISSO, CRIE DUAS LISTAS EXTRAS QUE VÃO CONTER APENAS 
# OS VALORES PARES E OS VALORES ÍMPARES DIGITADOS, RESPECTIVAMENTE. 
# AO FINAL, MOSTRE O CONTEÚDO DAS TRÊS LISTAS GERADAS.

print('\n\033[34m====== DESAFIO 82 ======\n\033[m')

valores = []
pares = []
impares = []

while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] ')).upper()[0]
    if resp == 'N':
        break 
for n in range(0,len(valores)):
    if valores[n] % 2 == 0:
        pares.append(valores[n])
    else:
        impares.append(valores[n])

# USANDO O FOR COM ENUMERATE:
#for i, v in enumerate(valores):
#    if v % 2 == 0:
#        pares.append(v)
#    else:
#        impares.append(v)

# SOLUÇÃO COLOCANDO O INPUT DIRETAMENTE NAS LISTAS DE PARES OU ÍMPARES
#while True:
#    num = int(input('Digite um valor: '))
#    valores.append(num)
#    if num % 2 ==0 :
#        pares.append(num)
#    else:
#        impares.append(num)
#    while True:
#        resp = str(input('Quer continuar? [S/N] ')).upper()[0]
#        if resp in 'SN':
#            break 
#    if resp == 'N':
#        break 

print('-='*30)
print(f'A lista completa é {valores}')
print(f'A lista de pares é {pares}')
print(f'A lista de ímpares é {impares}')
