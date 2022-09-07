# DESAFIO 071
# CRIE UM PROGRAMA QUE SIMULE O FUNCIONAMENTO DE UM CAIXA ELETRÔNICO. 
# NO INÍCIO, PERGUNTE AO USUÁRIO QUAL SERÁ O VALOR A SER SACADO (NÚMERO INTEIRO) 
# E O PROGRAMA VAI INFORMAR QUANTAS CÉDULAS DE CADA VALOR SERÃO ENTREGUES. 
# OBS: CONSIDERE QUE O CAIXA POSSUI CÉDULAS DE R$50, R$20, R$10 E R$1.

print('\n\033[34m====== DESAFIO 71 ======\n\033[m')

print('==== BANCO GUANABARA ====')
valor = int(input('Que valor você quer sacar? R$'))
cedula = 50
total_cedula = 0
while True:
    if valor >= cedula:
        valor -=cedula
        total_cedula += 1
    else:
        if total_cedula > 0:
            print(f'Total de {total_cedula} cédulas de R${cedula}.')
        if cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 1
        total_cedula = 0
        if valor == 0:
            break

# SOLUÇÃO SEM WHILE:

#cedulas_50 = valor//50
#print(f'Total de {cedulas_50} cédulas de R$50')
#cedulas_20 = (valor%50)//20
#print(f'Total de {cedulas_20} cédulas de R$20')
#cedulas_10 = ((valor%50)%20)//10
#print(f'Total de {cedulas_10} cédulas de R$10')
#cedulas_1 =(((valor%50)%20)%10)//1
#print(f'Total de {cedulas_1} cédulas de R$1')

print('='*25)
print('Volte sempre ao BANCO GUANABARA! Tenha um bom dia!')

