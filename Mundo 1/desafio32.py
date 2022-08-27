# DESAFIO 032
# FAÇA UM PROGRAMA QUE LEIA UM ANO QUALQUER E MOSTRE SE ELE É BISSEXTO.

from datetime import date
print('====== DESAFIO 32 ======')

ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual. '))
if ano == 0:
    ano = date.today().year

# Condição 1 : ser divisível por 400
c1 = ano % 400
# Condição 1 : ser divisível por 4
c2 = ano % 4  
# Condição 3 : ser divisível por 100
c3 = ano % 100

if c1 == 0:
#    print('Esse número é divisível por 400')
    print('O ano de {} é bissexto.'.format(ano))
else:
#    print('Esse número não é divisível por 400')
    if c2 == 0 and c3 > 0:
#        print('Esse número é divisível por 4 mas não é divisível por 100')
        print('O ano de {} é bissexto.'.format(ano))
    else: 
        print('O ano de {} não é bissexto.'.format(ano))

# outra solução com menos linhas de código:
# if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
#    print('O ano {} é BISSEXTO'.format(ano))
#else:
#    print('O ano {} NÃO é BISSEXTO'.format(ano))
