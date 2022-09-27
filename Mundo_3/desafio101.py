# DESAFIO 101
# CRIE UM PROGRAMA QUE TENHA UMA FUNÇÃO CHAMADA VOTO() 
# QUE VAI RECEBER COMO PARÂMETRO O ANO DE NASCIMENTO DE UMA PESSOA, 
# RETORNANDO UM VALOR LITERAL INDICANDO SE UMA PESSOA TEM VOTO NEGADO, 
# OPCIONAL E OBRIGATÓRIO NAS ELEIÇÕES.

print('\n\033[34m====== DESAFIO 101 ======\n\033[m')

def voto(anodenascimento):
    from datetime import date
    idade = date.today().year - anodenascimento
    print(f'Com {idade} anos: ', end='')
    if idade < 16:
        print('NÃO VOTA')
    elif 16 <= idade < 18 or idade > 70:
        print('VOTO FACULTATIVO')
    else: 
        print('VOTO OBRIGATÓRIO')
    

ano = int(input('Em que ano você nasceu? '))
voto(ano)