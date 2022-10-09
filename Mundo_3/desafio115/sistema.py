# DESAFIO 115
# CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS
# PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES.
# O SISTEMA SÓ VAI TER 2 OPÇÕES:
# CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS.

from lib115.interface115 import *
from time import sleep

print('\n\033[34m====== DESAFIO 115 ======\n\033[m')

while True:
    menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    opcao = leiaopcao('\033[32mSua Opção: \033[m')
    if opcao == 1 or opcao == 2:
        cabeçalho(f'OPÇÃO {opcao}')
    elif opcao == 3:
        cabeçalho(f'SAINDO DO SISTEMA ... ATÉ LOGO!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
