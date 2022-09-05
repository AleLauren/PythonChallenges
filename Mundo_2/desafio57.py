# DESAFIO 057
# FAÇA UM PROGRAMA QUE LEIA O SEXO DE UMA PESSOA, 
# MAS SÓ ACEITE OS VALORES ‘M’ OU ‘F’. 
# CASO ESTEJA ERRADO, PEÇA A DIGITAÇÃO NOVAMENTE ATÉ TER UM VALOR CORRETO.  

print('\n\033[34m====== DESAFIO 57 ======\n\033[m')

sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
# while sexo not in 'MmFf'
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso.'.format(sexo))
