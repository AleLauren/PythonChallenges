# DESAFIO 102
# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO FATORIAL() QUE RECEBA DOIS PARÂMETROS: 
# O PRIMEIRO QUE INDIQUE O NÚMERO A CALCULAR E OUTRO CHAMADO SHOW, 
# QUE SERÁ UM VALOR LÓGICO (OPCIONAL) INDICANDO SE SERÁ MOSTRADO 
# OU NÃO NA TELA O PROCESSO DE CÁLCULO DO FATORIAL.

print('\n\033[34m====== DESAFIO 102 ======\n\033[m')

def fatorial(num,show=False):
    """
    -> Calcula o Fatorial de um número.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    fat = 1
    for n in range(num,0,-1):
        fat *= n
        if show == True:
            print(n, end='')
            if n > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
    return fat


print(fatorial(6))
