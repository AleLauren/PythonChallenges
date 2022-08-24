# DESAFIO 008
# ESCREVA UM PROGRAMA QUE LEIA UM VALOR EM METROS 
# E O EXIBA CONVERTIDO EM CENTÍMETROS E MILÍMETROS

print('====== DESAFIO 08 ======')
m=float((input('Digite uma distância em metros: ')))

#solução 1:
#print('A medida de {}m corresponde a {:.0f}cm e {:.0f}mm.'.format(m,m*100,m*1000))

#solução 2 com outras unidades de medida:
print('A medida de {}m corresponde a: \n{:.4f}km \n{:.3f}hm \n{:.2f}dam \n{:.0f}dm \n{:.0f}cm \n{:.0f}mm'.format(m,m/1000,m/100,m/10,m*10,m*100,m*1000))