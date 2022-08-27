# DESAFIO 034
# ESCREVA UM PROGRAMA QUE PERGUNTE O SALÁRIO DE UM FUNCIONÁRIO 
# E CALCULE O VALOR DO SEU AUMENTO. PARA SALÁRIOS SUPERIORES A R$1250,00,
# CALCULE UM AUMENTO DE 10%. PARA OS INFERIORES OU IGUAIS, O AUMENTO É DE 15%.

print('====== DESAFIO 34 ======')

sal = float(input('Qual é o salário do funcionário? R$'))

if sal > 1250:
    novo_sal = sal*1.1
else:
    novo_sal = sal*1.15

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora' .format(sal,novo_sal))