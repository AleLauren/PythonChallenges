# DESAFIO 073
# CRIE UMA TUPLA PREENCHIDA COM OS 20 PRIMEIROS COLOCADOS 
# DA TABELA DO CAMPEONATO BRASILEIRO DE FUTEBOL, NA ORDEM DE COLOCAÇÃO. 
# DEPOIS MOSTRE:
# A) OS 5 PRIMEIROS TIMES.
# B) OS ÚLTIMOS 4 COLOCADOS.
# C) TIMES EM ORDEM ALFABÉTICA.
# D) EM QUE POSIÇÃO ESTÁ O TIME DA CHAPECOENSE.

print('\n\033[34m====== DESAFIO 73 ======\n\033[m')

tabela = ('Palmeiras','Flamengo','Corinthians','Internacional','Fluminense','Athletico-PR','Atlético-MG',
          'América-MG','Goiás','Santos','Bragantino','Fortaleza','Botafogo','São Paulo','Ceará','Cuiabá',
          'Coritiba','Avaí','Atlético-GO','Juventude')

print('-='*15)
print(f'Lista de times do Brasileirão: {tabela}')
print('-='*15)
print(f'Os 5 primeiros são: {tabela[0:5]}')
print('-='*15)
print(f'Os 4 últimos são: {tabela[-4:]}')
print('-='*15)
print(f'Times em ordem alfabética: {sorted(tabela)}')
print('-='*15)
print(f'O flamengo está na {tabela.index("Flamengo") + 1}ª posição')