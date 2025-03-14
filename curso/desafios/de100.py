from random import randint
lista = []
def sorteio(lista):
    for i in range(0,5):
        lista.append(randint(0,10))
    print(lista)

def soma(lista):
    s = 0
    for i in lista:
        if i % 2 == 0:
            s += i
    print(f'Somando os valores pares de {lista}, temos {s}')

sorteio(lista)
soma(lista)