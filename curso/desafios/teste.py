def notas(*notas, sit = False):
    r = dict()
    r['total'] = len(notas)
    r['maior'] = max(notas)
    r['menor'] = min(notas)
    r['media'] = sum(notas)/len(notas)
    
    return r


resp = notas(10, 6.7, 4.4)
print(resp)