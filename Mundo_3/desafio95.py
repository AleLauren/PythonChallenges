# DESAFIO 095
# APRIMORE O DESAFIO 93 PARA QUE ELE FUNCIONE COM VÁRIOS JOGADORES, 
# INCLUINDO UM SISTEMA DE VISUALIZAÇÃO DE DETALHES DO APROVEITAMENTO DE CADA JOGADOR.

print('\n\033[34m====== DESAFIO 95 ======\n\033[m')

performance = {}
gols = []
jogadores = []

while True: 
    performance.clear()
    gols.clear()
    performance['nome'] = input('Nome do jogador: ')
    p = int(input(f'Quantas partidas {performance["nome"]} jogou: '))
    for n in range(0,p):
        gols.append(int(input(f'Quantos gols na partida {n+1}? ')))
    performance['gols'] = gols[:]
    performance['total'] = sum(gols)
    jogadores.append(performance.copy())
    while True:
        cont = input('Quer continuar? [S/N] ').strip().upper()[0]
        if cont in 'SN':
            break
        print('ERRO! Responda apenas S ou N')
    print('-='*30)
    if cont == 'N':
        break

print('-'*60)
print(f'{"Cód":<5}', end='')
print(f'{"Nome":<25}', end='')
print(f'{"Gols":<25}', end='')
print(f'{"Total":<5}', end='')
print()
print('-'*60)
for n in range(len(jogadores)):
    print(f'{n+1:<5}', end='')
    print(f'{jogadores[n]["nome"]:<25}', end='')
    print(f'{str(jogadores[n]["gols"]):<25}', end='')
    print(f'{jogadores[n]["total"]:<5}', end='')
    print()
print('-'*60)
while True:
    cod = int(input('Mostrar dados de qual jogador? (999 para parar)'))
    if cod == 999:
        print('<< VOLTE SEMPRE! >>')
        break
    elif cod > len(jogadores):
        print(f'ERRO! Não existe jogador com código {cod}! Tente novamente')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {jogadores[cod-1]["nome"]}:')
        for g in range(0,len(jogadores[cod-1]["gols"])):
            print(f'No jogo {g+1} fez {jogadores[cod-1]["gols"][g]} gols.')
    print('-'*60)
