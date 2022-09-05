# DESAFIO 053
# CRIE UM PROGRAMA QUE LEIA UMA FRASE QUALQUER 
# E DIGA SE ELA É UM PALÍNDROMO, DESCONSIDERANDO OS ESPAÇOS. 

print('\033[34m====== DESAFIO 53 ======\n\033[m')

f = str(input('Digite uma frase: ')).strip()
frase = (f.replace(' ','')).upper()
print('O inverso de {} é {}'.format(frase, frase[::-1]))
if frase == frase[::-1]:
    print('Temos um PALÍNDROME!')
else:
    print('A frase: "{}" NÃO é um PALÍNDROME'.format(f))