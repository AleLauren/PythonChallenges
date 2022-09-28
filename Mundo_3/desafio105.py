# DESAFIO 105
# FAÇA UM PROGRAMA QUE TENHA UMA FUNÇÃO NOTAS() QUE PODE RECEBER VÁRIAS NOTAS DE ALUNOS 
# E VAI RETORNAR UM DICIONÁRIO COM AS SEGUINTES INFORMAÇÕES:    
# – QUANTIDADE DE NOTAS
# – A MAIOR NOTA
# – A MENOR NOTA
# – A MÉDIA DA TURMA
# – A SITUAÇÃO (OPCIONAL)

print('\n\033[34m====== DESAFIO 105 ======\n\033[m')

def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a situação da turma.
    """
    boletim = {}
    boletim['total'] = len(n)
    boletim['maior'] = max(n)
    boletim['menor'] = min(n)
    boletim['média'] = sum(n)/len(n)
    if sit == True:
        if boletim['média'] >= 7:
            boletim['situação'] = 'APROVADO'
        elif boletim['média'] >= 5:
            boletim['situação'] = 'RECUPERAÇÃO'
        else:
            boletim['situação'] = 'REPROVADO'
    return boletim


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
