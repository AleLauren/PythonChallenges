# DESAFIO 084
# FAÇA UM PROGRAMA QUE LEIA NOME E PESO DE VÁRIAS PESSOAS,
# GUARDANDO TUDO EM UMA LISTA. NO FINAL, MOSTRE:
# A) QUANTAS PESSOAS FORAM CADASTRADAS.     
# B) UMA LISTAGEM COM AS PESSOAS MAIS PESADAS.
# C) UMA LISTAGEM COM AS PESSOAS MAIS LEVES.

print('\n\033[34m====== DESAFIO 84 ======\n\033[m')

pessoas = []
ficha = []
lista_maior = []
lista_menor = []

while True:
    ficha.append(str(input('Nome: ')))
    ficha.append(float(input('Peso: ')))
    pessoas.append(ficha[:])
# Defino que o maior e o menor peso são iguais ao primeiro peso cadastrado
    if len(pessoas) == 1:
        maior = menor = ficha[1]
    ficha.clear()
    while True:
        cont = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if cont in 'SN':
            break
    if cont == 'N':
        break
print('-='*30)
# Varredura para definir o maior peso entre todos cadastrados
for p in pessoas:
    if p[1] > maior:
        maior = p[1]
    elif p[1] < menor:
        menor = p[1]
# Crio duas listas com os nomes das pessoas que tem os maiores e menores pesos
for p in pessoas:
    if p[1] == maior:
        lista_maior.append(p[0])
    elif p[1] == menor:
        lista_menor.append(p[0])
print(f'Ao todo, você cadastrou {len(pessoas)} pessoas.')
print(f'O maior peso foi de {maior}kg. Peso de {lista_maior}')
print(f'O menor peso foi de {menor}kg. Peso de {lista_menor}')