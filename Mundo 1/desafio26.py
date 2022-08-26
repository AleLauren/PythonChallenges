# DESAFIO 026
# FAÇA UM PROGRAMA QUE LEIA UMA FRASE PELO TECLADO 
# E MOSTRE QUANTAS VEZES APARECE A LETRA “A”, 
# EM QUE POSIÇÃO ELA APARECE A PRIMEIRA VEZ 
# E EM QUE POSIÇÃO ELA APARECE A ÚLTIMA VEZ.

print('====== DESAFIO 26 ======')

frase = str(input('Digite uma frase: ')).strip().lower()
# Quantas vezes aparece a letra a
print('A letra A aparece {} vez(es) na frase.' .format(frase.count('a')))
#Em que posição aparece a primeira vez
a1 = int(frase.find('a'))
print('A primeira letra A apareceu na posição {}.' .format(a1+1))
#Em que posição aparece a última vez
au = int(frase.rfind('a'))
print('A última letra A apareceu na posição {}.' .format(au+1))

# outra solução :
# frase_invertida = frase[::-1]
# au = int(frase_invertida.find('a'))
# print('A última letra A apareceu na posição {}.' .format(len(frase)-au))


