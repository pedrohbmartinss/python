def voto(a):
    import datetime
    idade = datetime.date.today().year - a
    print(idade)
    if idade < 16:
        return f'Com {idade} anos, seu voto é negado'
    elif idade < 18 or idade > 70:
        return f'Com {idade} anos, seu voto é opcional'
    else:
        return f'Com {idade} anos, seu voto é obrigatório'


ano = int(input('Em que ano você nasceu?'))
print(voto(ano))