# DESAFIO 063
# ESCREVA UM PROGRAMA QUE LEIA UM NÚMERO N INTEIRO QUALQUER 
# E MOSTRE NA TELA OS N PRIMEIROS ELEMENTOS DE UMA SEQUÊNCIA DE FIBONACCI. 
# EXEMPLO: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('\n\033[34m====== DESAFIO 63 ======\n\033[m')

print('='*24)
print('{:^24}'.format('SEQUÊNCIA DE FIBONACCI'))
print('='*24)
n = int(input('Quantos termos você quer mostrar? '))
n1 = 0
n2 = 1
x = 0
print('~'*24)
if n == 0:
    print('FIM')
elif n == 1:
    print('{} → FIM' .format(n1))
elif n == 2:
    print('{} → {} → FIM' .format(n1,n2))
else:
    print('0 → 1 → ', end='')
    while x < n-2:
        soma = n1 + n2
        print('{} → ' .format(soma), end='')
        x += 1
        n1 = n2
        n2 = soma
    print('FIM')
print('~'*24)