# DESAFIO 097
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA ESCREVA(), 
# QUE RECEBA UM TEXTO QUALQUER COMO PARÂMETRO E MOSTRE UMA MENSAGEM COM TAMANHO ADAPTÁVEL.       
# EX:
# ESCREVA(‘OLÁ, MUNDO!’) SAÍDA: 
#  ~~~~~~~~~
# OLÁ, MUNDO!       
#  ~~~~~~~~~

print('\n\033[34m====== DESAFIO 97 ======\n\033[m')

def escreva(msg):
    print('~'*(len(msg)+2))
    print(f' {msg}')
    print('~'*(len(msg)+2))

msg = str(input('Digite a mensagem que deseja formatar: '))
escreva(msg)