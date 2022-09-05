# DESAFIO 039
# FAÇA UM PROGRAMA QUE LEIA O ANO DE NASCIMENTO DE UM JOVEM 
# E INFORME, DE ACORDO COM A SUA IDADE, SE ELE AINDA VAI SE ALISTAR AO SERVIÇO MILITAR, 
# SE É A HORA EXATA DE SE ALISTAR OU SE JÁ PASSOU DO TEMPO DO ALISTAMENTO. 
# SEU PROGRAMA TAMBÉM DEVERÁ MOSTRAR O TEMPO QUE FALTA OU QUE PASSOU DO PRAZO.

from datetime import date
print('====== DESAFIO 39 ======')

ano_nasc = int(input('Ano de Nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nasc

print('Quem nasceu em {} tem {} anos até o fim de {}.'.format(ano_nasc, idade, ano_atual))

if idade == 18:
    print('Você precisa se alistar ESTE ANO!')
elif idade > 18:
    print("""Você já deveria ter se alistado há {} anos. 
Seu alistamento foi em {}""" .format(idade-18, ano_atual-(idade-18)))
elif idade < 18:
    print("""Ainda faltam {} anos para o alistamento.
Seu alistamento será em {}""".format(18-idade,ano_atual+(18-idade)))
