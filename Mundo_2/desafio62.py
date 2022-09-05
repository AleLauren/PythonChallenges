# DESAFIO 062
# MELHORE O DESAFIO 61, PERGUNTANDO PARA O USUÁRIO 
# SE ELE QUER MOSTRAR MAIS ALGUNS TERMOS. 
# O PROGRAMA ENCERRARÁ QUANDO ELE DISSER QUE QUER MOSTRAR 0 TERMOS.

print('\n\033[34m====== DESAFIO 62 ======\n\033[m')

print('='*24)
print('{:^24}'.format('GERADOR DE PA'))
print('='*24)
n1 = int(input('Primeiro termo: '))
r = int(input('Razão: '))
# x é o contador
x = 0
# número inicial de termos da PA que serão mostrados
n_termos = 10
# incremento de termos da PA que serão mostrados posteriormente
incremento = 1
while incremento !=0:
    while x < n_termos:
        n = n1 + x*r
        print("{} → ".format(n) , end="")
        x += 1
    print('PAUSA')
    incremento = int(input('Quantos termos você quer mostrar a mais? '))
    n_termos += incremento
print('Progressão finalizada com {} termos mostrados.'.format(n_termos))