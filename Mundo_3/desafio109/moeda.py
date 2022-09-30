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
