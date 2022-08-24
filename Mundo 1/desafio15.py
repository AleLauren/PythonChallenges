# DESAFIO 015
# ESCREVA UM PROGRAMA QUE PERGUNTE A QUANTIDADE DE KM PERCORRIDOS POR UM CARRO ALUGADO
# E A QUANTIDADE DE DIAS PELOS QUAIS ELE FOI ALUGADO. CALCULE O PREÇO A PAGAR
# SABENDO QUE O CARRO CUSTA R$60 POR DIA E R$0.15 POR KM RODADO.

print('====== DESAFIO 15 ======')

d=int(input('Quantos dias alugados? '))
km=float(input('Quantos km rodados? '))
p=60*d+0.15*km
print('O total a pagar é de R${:.2f}'.format(p))