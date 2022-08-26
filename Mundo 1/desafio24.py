# DESAFIO 024
# CRIE UM PROGRAMA QUE LEIA O NOME DE UMA CIDADE 
# E DIGA SE ELA COMEÇA OU NÃO COM O NOME “SANTO”

print('====== DESAFIO 24 ======')

cidade = str(input('Em que cidade você nasceu? ')).strip()
print('santo' in cidade.lower()[:5])
# outra solução:
#print(cidade[:5].upper() == 'SANTO')