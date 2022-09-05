# DESAFIO 011
# FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS,
# CALCULE A SUA ÁREA E A QUANTIDADE DE TINTA NECESSÁRIA PARA PINTÁ-LA,
# SABENDO QUE CADA LITRO DE TINTA PINTA UMA ÁREA DE 2M².

print('====== DESAFIO 11 ======')
l=float(input('Qual a largura da parede? '))
a=float(input('Qual a altura da parede? '))
area=l*a
tinta=(area/2)
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(l,a,area))
print('Para pintar essa parede você precisará de {:.2f}l de tinta'.format(tinta))