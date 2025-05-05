def notas(*notas, sit = False):
    """
    funcao para adicionar quantas notas quiser e bla bla bla

    """
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas)/len(notas)
    if sit:
        if r['media'] >= 7:
            r['situacao'] = 'BOA'
        elif r['media'] >= 5:
            r['situacao'] = 'RAZOAVEL'
        else:
            r['situacao'] = 'RUIM'
    
    return r


resp = notas(5, 3.7, 4.4, sit = True)
print(resp)
help(notas)