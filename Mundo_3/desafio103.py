# DESAFIO 103
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA FICHA(), 
# QUE RECEBA DOIS PARÂMETROS OPCIONAIS: O NOME DE UM JOGADOR E QUANTOS GOLS ELE MARCOU. 
# O PROGRAMA DEVERÁ SER CAPAZ DE MOSTRAR A FICHA DO JOGADOR, 
# MESMO QUE ALGUM DADO NÃO TENHA SIDO INFORMADO CORRETAMENTE.

print('\n\033[34m====== DESAFIO 103 ======\n\033[m')

def ficha(nome='<desconhecido>',gols=0):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato.')


n = str(input('Nome do Jogador: ')).strip()
g = str(input('Número de Gols: '))
if g.isnumeric():
    g = int(g)
else:
    g = 0
if n == '':
    ficha(gols=g)
else:
    ficha(n,g)
    