# DESAFIO 031
# DESENVOLVA UM PROGRAMA QUE PERGUNTE A DISTÂNCIA DE UMA VIAGEM EM KM. 
# CALCULE O PREÇO DA PASSAGEM, COBRANDO R$0,50 POR KM PARA 
# VIAGENS DE ATÉ 200KM E R$0,45 PARA VIAGENS MAIS LONGAS.

print('====== DESAFIO 31 ======')

dist = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}km'.format(dist))

if dist<=200 :
    preco = dist*0.5
    print('E o preço de sua passagem será de R${:.2f}' .format(preco))
else:
    preco = dist*0.45
    print('E o preço de sua passagem será de R${:.2f}' .format(preco))

