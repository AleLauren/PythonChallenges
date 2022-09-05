# DESAFIO 007
# DESENVOLVA UM PROGRAMA QUE LEIA AS DUAS NOTAS DE UM ALUNO,
# CALCULE E MOSTRE A SUA MÉDIA.

print('====== DESAFIO 07 ======')
P1=(input('Digite a nota da P1: '))
P2=(input('Digite a nota da P2: '))
M=((float(P1)+float(P2))/2)
print('A média entre {} e {} é {:.1f}'.format(P1,P2,M))