# DESAFIO 093
# CRIE UM PROGRAMA QUE GERENCIE O APROVEITAMENTO DE UM JOGADOR DE FUTEBOL. 
# O PROGRAMA VAI LER O NOME DO JOGADOR E QUANTAS PARTIDAS ELE JOGOU. 
# DEPOIS VAI LER A QUANTIDADE DE GOLS FEITOS EM CADA PARTIDA. 
# NO FINAL, TUDO ISSO SERÁ GUARDADO EM UM DICIONÁRIO, 
# INCLUINDO O TOTAL DE GOLS FEITOS DURANTE O CAMPEONATO.

print('\n\033[34m====== DESAFIO 93 ======\n\033[m')

performance = {}
gols = []

performance['nome'] = input('Nome do jogador: ')
p = int(input(f'Quantas partidas {performance["nome"]} jogou: '))
for n in range(0,p):
    gols.append(int(input(f'Quantos gols na partida {n+1}? ')))
print('-='*30)
performance['gols'] = gols[:]
performance['total'] = sum(gols)
print(performance)
print('-='*30)
for k,v in performance.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)
print(f'O jogador {performance["nome"]} jogou {len(performance["gols"])} partidas.')
for n in range(0,len(performance["gols"])):
    print(f'    => Na partida {n+1}, fez {gols[n]} gols.')
print(f'Foi um total de {performance["total"]} gols.')