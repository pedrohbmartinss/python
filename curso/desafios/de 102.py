def fatorial(num, show = False):
    """
    Calcula o fatorial de um numero inteiro:
    num = numero que quer ser calculado o fatorial
    show = parametro que fiz se o calculo quer ser mostrado
    return = nao tem return
    """
    f = 1
    for i in range(num, 1, -1):
        f = f * i
        if show == True:
            print(f'{i} x ', end = '')
    if show == True:
        print(f'{1} = ', end = '')
    print(f'{f}')


num = int(input('Deseja o fatorial de qual numero? '))
show = ''
help(fatorial)
fatorial(num, show=True)
