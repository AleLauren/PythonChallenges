# DESAFIO 010
# CRIE UM PROGRAMA QUE LEIA QUANTO DINHEIRO 
# UMA PESSOA TEM NA CARTEIRA E MOSTRE
# QUANTOS DÓLARES ELA PODE COMPRAR.

print('====== DESAFIO 10 ======')
r=float(input('Quanto dinheiro você tem na carteira? R$'))
# taxa de câmbio => dólar hoje : 1 dólar = 5.11 reais
c=float(5.11)
print('Com {:.2f} reais é possível comprar {:.2f} dólares'.format(r,r/c))