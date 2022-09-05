# DESAFIO 054
# CRIE UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE SETE PESSOAS. 
# NO FINAL, MOSTRE QUANTAS PESSOAS AINDA NÃO ATINGIRAM A MAIORIDADE 
# E QUANTAS JÁ SÃO MAIORES.

print('\033[34m====== DESAFIO 54 ======\n\033[m')

from datetime import date

ano_atual = date.today().year
maioridade = 0
menoridade = 0

for n in range (1,8):
    ano_nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(n)))
    if ano_atual - ano_nasc >= 21:
        maioridade += 1
    else:
        menoridade += 1

print('Ao todo tivemos {} pessoas maiores de idade'.format(maioridade))
print('E também tivemos {} pessoas menores de idade'.format(menoridade))


