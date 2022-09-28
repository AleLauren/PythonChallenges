# DESAFIO 106
# FAÇA UM MINI-SISTEMA QUE UTILIZE O INTERACTIVE HELP DO PYTHON. 
# O USUÁRIO VAI DIGITAR O COMANDO E O MANUAL VAI APARECER. 
# QUANDO O USUÁRIO DIGITAR A PALAVRA ‘FIM’, O PROGRAMA SE ENCERRARÁ. IMPORTANTE: USE CORES.

from time import sleep

print('\n\033[34m====== DESAFIO 106 ======\n\033[m')

c = ('\033[m',             # 0 - sem cores
     '\033[0;30;41m',      # 1 - vermelho
     '\033[0;30;42m',      # 2 - verde
     '\033[0;30;43m',      # 3 - amarelo
     '\033[0;30;44m',      # 4 - azul
     '\033[0;30;45m',      # 5 - roxo
     '\033[7;30'           # 6 - branco
    );

def titulo(msg, cor=0):
    print(c[cor], end='')
    print('~'*(len(msg)+2))
    print(f' {msg} ')
    print('~'*(len(msg)+2))
    print(c[0], end='')
    sleep(1)


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print()
    print(c[3], end='', flush=True)
    help(com)
    print(c[0], end='', flush=True)
    sleep(2)


comando = ''
while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input("Função ou Biblioteca > "))
    if comando.upper().strip() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('ATÉ LOGO!', 1)
