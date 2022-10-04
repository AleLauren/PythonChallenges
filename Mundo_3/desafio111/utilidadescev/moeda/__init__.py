def moeda(preço = 0, moeda = 'R$'):
    res = f'{moeda}{preço:.2f}'.replace('.',',')
    return res


def aumentar(preço = 0, taxa = 0, formatacao=False):
    res = preço * (1+(taxa/100))
    return res if formatacao is False else moeda(res)


def diminuir(preço = 0, taxa = 0, formatacao=False):
    res = preço * (1-(taxa/100))
    return res if not formatacao else moeda(res)


def dobro(preço = 0, formatacao=False):
    res = 2*preço
    return res if not formatacao else moeda(res)


def metade(preço = 0, formatacao=False):
    res = preço/2
    return res if not formatacao else moeda(res)


def resumo(preço = 0, taxa_a = 10, taxa_d = 5):
    print('-'*32)
    print('RESUMO DO VALOR'.center(32))
    print('-'*32)
#OUTRA MANEIRA DE FAZER TABULAÇÃO: \t
#   print(f'Preço analisado: \t{moeda(preço)}')
    print(f'{"Preço analisado:":<20}{moeda(preço):<12}')
    print(f'{"Dobro do preço:":<20}{dobro(preço,True):<12}')
    print(f'{"Metade do preço:":<20}{metade(preço,True):<12}')
    print(f'{taxa_a:>2}{"% de aumento:":<18}{aumentar(preço,taxa_a,True):<12}')
    print(f'{taxa_d:>2}{"% de redução":<18}{diminuir(preço,taxa_d,True):<12}')
    print('-'*32)
