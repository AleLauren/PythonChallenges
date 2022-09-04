# DESAFIO 059
# CRIE UM PROGRAMA QUE LEIA DOIS VALORES E MOSTRE UM MENU NA TELA:

#[ 1 ] SOMAR
#[ 2 ] MULTIPLICAR
#[ 3 ] MAIOR
#[ 4 ] NOVOS NÚMEROS
#[ 5 ] SAIR DO PROGRAMA

# SEU PROGRAMA DEVERÁ REALIZAR A OPERAÇÃO SOLICITADA EM CADA CASO.

print('\n\033[34m====== DESAFIO 59 ======\n\033[m')

n1 = float(input('Primeiro valor: '))
n2 = float(input('Segundo valor: '))
operacao = 0
while operacao != 5:
    print("""[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA""")
    operacao = int(input('>>>>> Qual é a sua opção? '))
    if operacao == 1:
        print('A soma de {} e {} é {}.' .format(n1,n2,n1+n2))
    elif operacao == 2:
        print('A multiplicação de {} e {} é {}.' .format(n1,n2,n1*n2))
    elif operacao == 3:
        if n1>n2:
            maior = n1
        else: 
            maior = n2
        print('O maior número entre {} e {} é {}.' .format(n1,n2,maior))
    elif operacao == 4:
        print('Ok, vamos tentar de novo com novos números!')
        n1 = float(input('Primeiro valor: '))
        n2 = float(input('Segundo valor: '))
    elif operacao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')
    print('-=-'*19)        
print('Fim do programa! Volte sempre!')