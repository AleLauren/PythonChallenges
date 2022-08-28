# DESAFIO 040
# CRIE UM PROGRAMA QUE LEIA DUAS NOTAS DE UM ALUNO E CALCULE SUA MÉDIA, 
# MOSTRANDO UMA MENSAGEM NO FINAL, DE ACORDO COM A MÉDIA ATINGIDA:
#– MÉDIA ABAIXO DE 5.0: REPROVADO
#– MÉDIA ENTRE 5.0 E 6.9: RECUPERAÇÃO
#– MÉDIA 7.0 OU SUPERIOR: APROVADO

print('====== DESAFIO 40 ======')

P1=float(input('Digite a nota da P1: '))
P2=float(input('Digite a nota da P2: '))
M=(P1+P2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(P1,P2,M))
if M >= 7:
    print('O aluno está APROVADO')
elif 7 > M >= 5:
    print('O aluno está em RECUPERAÇÃO')
elif M < 5:
    print('O aluno está REPROVADO')
