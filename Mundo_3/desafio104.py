# DESAFIO 104
# CRIE UM PROGRAMA QUE TENHA A FUNÇÃO LEIAINT(), 
# QUE VAI FUNCIONAR DE FORMA SEMELHANTE ‘A FUNÇÃO INPUT() DO PYTHON, 
# SÓ QUE FAZENDO A VALIDAÇÃO PARA ACEITAR APENAS UM VALOR NUMÉRICO. 
# EX: N = LEIAINT(‘DIGITE UM N: ‘)

print('\n\033[34m====== DESAFIO 104 ======\n\033[m')

def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            valor = int(num)
            return valor
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
