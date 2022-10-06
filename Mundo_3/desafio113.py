# DESAFIO 113
# REESCREVA A FUNÇÃO LEIAINT() QUE FIZEMOS NO DESAFIO 104, 
# INCLUINDO AGORA A POSSIBILIDADE DA DIGITAÇÃO DE UM NÚMERO DE TIPO INVÁLIDO. 
# APROVEITE E CRIE TAMBÉM UMA FUNÇÃO LEIAFLOAT() COM A MESMA FUNCIONALIDADE.

print('\n\033[34m====== DESAFIO 113 ======\n\033[m')

def leiaint(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO! Digite um número real válido.\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n


n_int = leiaint('Digite um número inteiro: ')
n_fl = leiafloat('Digite um número real: ')
print(f'Você acabou de digitar o número inteiro {n_int} e o número real {n_fl}')
