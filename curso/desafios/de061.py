t1 = int(input('Qual o primeiro termo?: '))
razao = int(input('Qual a razao: '))
i = 0
vezes = 0

while vezes < 10:
    vezes += 1
    print(t1 + i)
    i += razao
amais = int(input('Quantos termos você quer mostrar a mais?: '))
vezes = 0
while vezes < amais:
    vezes += 1
    print(t1 + i)
    i += razao