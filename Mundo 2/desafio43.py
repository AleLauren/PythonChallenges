# DESAFIO 043
# DESENVOLVA UMA LÓGICA QUE LEIA O PESO E A ALTURA DE UMA PESSOA, 
# CALCULE SEU ÍNDICE DE MASSA CORPORAL (IMC) 
# E MOSTRE SEU STATUS, DE ACORDO COM A TABELA ABAIXO:
#– IMC ABAIXO DE 18,5: ABAIXO DO PESO
#– ENTRE 18,5 E 25: PESO IDEAL
#– 25 ATÉ 30: SOBREPESO
#– 30 ATÉ 40: OBESIDADE
#– ACIMA DE 40: OBESIDADE MÓRBIDA

print('====== DESAFIO 43 ======')

peso = float(input('Qual é seu peso? (Kg) '))
altura = float(input('Qual é sua altura? (m) '))

# FÓRMULA DO IMC = PESO / (ALTURA**2)
imc = peso / (altura**2)
print('O seu IMC é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO DO PESO normal.') 
elif 18 <= imc < 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc < 40:
    print('Você está em OBESIDADE!')
elif imc >=40 :
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')
