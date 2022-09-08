# DESAFIO 072
# CRIE UM PROGRAMA QUE TENHA UMA TUPLA TOTALMENTE PREENCHIDA 
# COM UMA CONTAGEM POR EXTENSO, DE ZERO ATÉ VINTE. 
# SEU PROGRAMA DEVERÁ LER UM NÚMERO PELO TECLADO (ENTRE 0 E 20) E MOSTRÁ-LO POR EXTENSO

print('\n\033[34m====== DESAFIO 72 ======\n\033[m')

num = ('zero','um','dois','três','quatro','cinco','seis','sete','oito',
       'nove','dez','onze','doze','treze','catorze','quinze','dezesseis',
       'dezessete','dezoito','dezenove','vinte')
num_fr = ('zéro','un','deux','trois','quatre','cinq','six','sept','huit',
          'neuf','dix','onze','douze','treize','quatorze','quinze','seize',
          'dix-sept','dix-huit','dix-neuf','vingt')

while True:
    cont = ' '
    n = int(input('Digite um número entre 0 e 20: ').strip())
    if 0<= n <= 20:
        while True:
# adicionei a opção de mostrar o número por extenso em dois idiomas, português e francês:
            lang = input('Em que idioma você gostaria de ver o número? [PT/FR] ').strip().upper()[0:2]
            if lang not in 'PTPOFR':
                print('Idioma não identificado')
            else:
                if lang == 'FR':
                    print(f'Você digitou o número {num_fr[n]}')
                else:
                    print(f'Você digitou o número {num[n]}')
                break
        while True:
            cont = input('Deseja continuar? [S/N] ').strip()[0]
            if cont not in 'SsNn':
                print('Opção inválida.')
            else:
                break    
    if cont in 'Nn':
        break
    if cont == ' ':
        print('Tente novamente. ' , end='')
