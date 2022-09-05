# DESAFIO 004
# FAÇA UM PROGRAMA QUE LEIA ALGO PELO TECLADO E MOSTRE NA TELA
# O SEU TIPO PRIMITIVO E TODAS AS INFORMAÇÕES POSSÍVEIS SOBRE ELE.

print('====== DESAFIO 04 ======')
x = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(x))
print('Só tem espaços?', x.isspace())
print('É um número?', x.isnumeric())
print('É alfabético?', x.isalpha())
print('É alfanumérico?', x.isalnum())
print('Está em maiúsculas?', x.isupper())
print('Está em minúsculas?', x.islower())
print('Está capitalizada?', x.istitle())