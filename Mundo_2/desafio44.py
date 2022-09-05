# DESAFIO 044
# ELABORE UM PROGRAMA QUE CALCULE O VALOR A SER PAGO POR UM PRODUTO, 
# CONSIDERANDO O SEU PREÇO NORMAL E CONDIÇÃO DE PAGAMENTO:

#– À VISTA DINHEIRO/CHEQUE: 10% DE DESCONTO
#– À VISTA NO CARTÃO: 5% DE DESCONTO
#– EM ATÉ 2X NO CARTÃO: PREÇO FORMAL
#– 3X OU MAIS NO CARTÃO: 20% DE JUROS

print('====== DESAFIO 44 ======')

print('==== LOJAS GUANABARA ====')
valor = float(input('Preço das compras: R$'))
print("""FORMAS DE PAGAMENTO
[ 1 ] à vista dinheiro / cheque
[ 2 ] à vista cartão
[ 3 ] 2x no cartão
[ 4 ] 3x ou mais no cartão""")
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    vf = valor * 0.9
elif opcao == 2:
    vf = valor * 0.95
elif opcao == 3: 
    vf = valor
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS.'.format(vf/2))
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    vf = valor * 1.2
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS.'.format(parcelas, vf/parcelas))
else:
    vf = valor
    print('Opção INVÁLIDA. Tente novamente!')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, vf))

