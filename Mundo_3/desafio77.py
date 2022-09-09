# DESAFIO 077
# CRIE UM PROGRAMA QUE TENHA UMA TUPLA COM VÁRIAS PALAVRAS (NÃO USAR ACENTOS). 
# DEPOIS DISSO, VOCÊ DEVE MOSTRAR, PARA CADA PALAVRA, QUAIS SÃO AS SUAS VOGAIS.


print('\n\033[34m====== DESAFIO 77 ======\033[m')
palavras = ('aprender','programar','linguagem','python',
            'curso','gratis','estudar','praticar',
            'trabalhar','mercado','programador','futuro')
for n in palavras:
    print(f'\nNa palavra {n.upper()} temos ', end='')
    for letra in n:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')