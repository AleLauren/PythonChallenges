# DESAFIO 114
# CRIE UM CÓDIGO EM PYTHON QUE TESTE SE O SITE PUDIM ESTÁ ACESSÍVEL PELO COMPUTADOR USADO.

print('\n\033[34m====== DESAFIO 114 ======\n\033[m')

import urllib.request

try:
    pudim=urllib.request.urlopen('http://www.pudim.com.br')
except urllib.request.URLError:
    print('O site PUDIM está acessível no momento.')
else:
    print('O site PUDIM está acessível!')
# PARA LER O CÓDIGO DO SITE
#    print(pudim.read())

# PARA VERIFICAR SE QUALQUER SITE ESTÁ DISPONÍVEL:
site=str(input('Deseja verificar outro site? Insira o site: '))
try:
    site1=urllib.request.urlopen('http://www.'+site+'/')
except urllib.request.URLError:
    print('O site não está acessível no momento.')
else:
    print('O site está acessível!')