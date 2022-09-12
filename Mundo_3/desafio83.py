# DESAFIO 083
# CRIE UM PROGRAMA ONDE O USUÁRIO DIGITE UMA EXPRESSÃO QUALQUER QUE USE PARÊNTESES. 
# SEU APLICATIVO DEVERÁ ANALISAR SE A EXPRESSÃO PASSADA 
# ESTÁ COM OS PARÊNTESES ABERTOS E FECHADOS NA ORDEM CORRETA.

print('\n\033[34m====== DESAFIO 83 ======\n\033[m')

exp = str(input('Digite uma expressão: ')).strip()
lista = []
for carac in exp:
    if carac == '(':
        lista.append('(')
    elif carac == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')
    
# SOLUÇÃO SIMPLES SEM LISTA
#if exp.count('(') != exp.count(')'):
#    print('Sua expressão está errada!')
#else:
#    print('Sua expressão está válida')

