# DESAFIO 098
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA CONTADOR(), QUE RECEBA TRÊS PARÂMETROS: 
# INÍCIO, FIM E PASSO. SEU PROGRAMA TEM QUE REALIZAR TRÊS CONTAGENS ATRAVÉS DA FUNÇÃO CRIADA:
# A) DE 1 ATÉ 10, DE 1 EM 1
# B) DE 10 ATÉ 0, DE 2 EM 2
# C) UMA CONTAGEM PERSONALIZADA

from time import sleep

print('\n\033[34m====== DESAFIO 98 ======\n\033[m')

def contador(i,f,p):
    print('-='*30)
    if p < 0:
        p = p*(-1)
    elif p == 0:
        p = 1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    sleep(2.5)
    if f < i:
        for n in range(i,f-1,-p):
# As you do not have a newline in your string, python will buffer it. 
# You have to explicitly flush the output after each character using flush=True
            print(n, end=' ', flush=True)
            sleep(0.5)
    else:
        for n in range(i,f+1,p):
            print(n, end=' ', flush=True)
            sleep(0.5)
    print('FIM!')
    sleep(1)


contador(1, 10, 1)
contador(10, 0, 2)
print('-='*30)
print('Agora é sua vez de personalizar a contagem!')
i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)

