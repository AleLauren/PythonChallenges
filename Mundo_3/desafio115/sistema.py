# DESAFIO 115
# CRIE UM PEQUENO SISTEMA MODULARIZADO QUE PERMITA CADASTRAR PESSOAS
# PELO SEU NOME E IDADE EM UM ARQUIVO DE TEXTO SIMPLES.
# O SISTEMA SÓ VAI TER 2 OPÇÕES:
# CADASTRAR UMA NOVA PESSOA E LISTAR TODAS AS PESSOAS CADASTRADAS.

from lib115.interface115 import *
from lib115.arquivo115 import *
from time import sleep

print('\n\033[34m====== DESAFIO 115 ======\n\033[m')

arq = 'cadastros.txt'
if not arquivoExiste(arq):
    criarArquivo(arq)
    
while True:
    menu(['Ver pessoas cadastradas','Cadastrar nova Pessoa','Sair do Sistema'])
    opcao = leiaint('\033[32mSua Opção: \033[m')
    if opcao == 1:
        # Mostra o contéudo do banco de dados cadastros.txt
        lerArquivo(arq)
    elif opcao == 2:
        # Cadastra uma nova pessoa
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        idade = leiaint('Idade: ')
        cadastrar(arq, nome, idade)
    elif opcao == 3:
        cabeçalho('SAINDO DO SISTEMA ... ATÉ LOGO!')
        break
    else:
        print('\033[0;31mERRO! Digite uma opção válida.\033[m')
    sleep(2)
