# DESAFIO 070
# CRIE UM PROGRAMA QUE LEIA O NOME E O PREÇO DE VÁRIOS PRODUTOS. 
# O PROGRAMA DEVERÁ PERGUNTAR SE O USUÁRIO VAI CONTINUAR OU NÃO. 
# NO FINAL, MOSTRE:
# A) QUAL É O TOTAL GASTO NA COMPRA.
# B) QUANTOS PRODUTOS CUSTAM MAIS DE R$1000.
# C) QUAL É O NOME DO PRODUTO MAIS BARATO.

print('\n\033[34m====== DESAFIO 70 ======\n\033[m')

print('==== LOJAS GUANABARA ====')

total = prod_1k = preco_pechincha = 0
pechincha = ' '

while True:
    produto = str(input('Nome do Produto: ')).strip().capitalize()
    preco = float(input('Preço: R$'))
    if total == 0 or preco < preco_pechincha:
        pechincha = produto
        preco_pechincha = preco
    total += preco
    if preco > 1000:
        prod_1k += 1 
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('==== FIM DO PROGRAMA ====')
print(f"""O total da compra foi R${total:.2f}
Temos {prod_1k} produtos custando mais de R$1000.00
O produto mais barato foi {pechincha} que custa R${preco_pechincha:.2f}""")