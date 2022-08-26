# DESAFIO 027
# FAÇA UM PROGRAMA QUE LEIA O NOME COMPLETO DE UMA PESSOA, 
# MOSTRANDO EM SEGUIDA O PRIMEIRO E O ÚLTIMO NOME SEPARADAMENTE.

print('====== DESAFIO 27 ======')

n = str(input('Digite seu nome completo: ')).strip().lower()
print('Muito prazer em te conhecer!')
nome = n.split() 
#print(len(nome)) => len(nome) mostra quantos elementos tem essa lista
#neste caso, mostra quantos nomes / sobrenomes a pessoa tem
print('Seu primeiro nome é {}'.format(nome[0].capitalize()))
print('Seu último nome é {}'.format(nome[len(nome)-1].capitalize()))

# outra solução: 
# O "[::-1]" inverte a string
# como não sabemos quantos sobrenomes a pessoa tem,
#invertemos e pegamos a primeira palavra (que antes era a última)
#nome_inv = n[::-1].split()
#sobrenome_inv = nome_inv[0]
#print('Seu último nome é {}'.format(sobrenome_inv[::-1].capitalize()))
