def moeda(preço = 0, moeda = 'R$'):
    res = f'{moeda}{preço:.2f}'.replace('.',',')
    return res


def aumentar(preço = 0, taxa = 0):
    res = preço * (1+(taxa/100))
    return res


def diminuir(preço = 0, taxa = 0):
    res = preço * (1-(taxa/100))
    return res


def dobro(preço = 0):
    res = 2*preço
    return res


def metade(preço = 0):
    res = preço/2
    return res
    