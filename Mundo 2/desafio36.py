# DESAFIO 036
# ESCREVA UM PROGRAMA PARA APROVAR O EMPRÉSTIMO BANCÁRIO PARA A COMPRA DE UMA CASA. 
# PERGUNTE O VALOR DA CASA, O SALÁRIO DO COMPRADOR E EM QUANTOS ANOS ELE VAI PAGAR.
# A PRESTAÇÃO MENSAL NÃO PODE EXCEDER 30% DO SALÁRIO OU ENTÃO O EMPRÉSTIMO SERÁ NEGADO.

print('====== DESAFIO 36 ======')

valor = float(input('Valor da casa: R$ '))
salario = float(input('Salário do comprador: R$ '))
anos = float(input('Quantos anos de financiamento? ')) 
prestacao = valor / (anos*12)

print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(valor,anos,prestacao))
if prestacao > (salario*0.3):
    print('Empréstimo NEGADO!')
else:
    print('Empréstimo pode ser CONCEDIDO!')