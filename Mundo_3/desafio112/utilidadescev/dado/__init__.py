def leiaDinheiro(msg):
    válido = False
    while not válido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.count('.') == 1 and len(entrada) > 1 and entrada.find('.')!=0 and entrada.replace('.', '0').isnumeric():
            válido = True
            return float(entrada)
        elif entrada.isnumeric():
            válido = True
            return float(entrada)
        else:
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!\033[m')
