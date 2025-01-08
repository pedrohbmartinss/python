n1 = int(input('primeiro valor: '))
n2 = int(input('segundo valor: '))
n3 = int(input('terceiro valor: '))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('\033[32mO maior valor é {}'.format(maior))
print('\033[31mO menor valor é {}\033[m'.format(menor))  