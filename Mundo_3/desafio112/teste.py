# DESAFIO 112
# DENTRO DO PACOTE UTILIDADESCEV QUE CRIAMOS NO DESAFIO 111, TEMOS UM MÓDULO CHAMADO DADO. 
# CRIE UMA FUNÇÃO CHAMADA LEIADINHEIRO() QUE SEJA CAPAZ DE FUNCIONAR COMO A FUNÇÃO IMPUTA(), 
# MAS COM UMA VALIDAÇÃO DE DADOS PARA ACEITAR APENAS VALORES QUE SEJA MONETÁRIOS.

from utilidadescev import moeda, dado

print('\n\033[34m====== DESAFIO 112 ======\n\033[m')

p = dado.leiaDinheiro('Digite o preço: R$')
moeda.resumo(p,35,22)
