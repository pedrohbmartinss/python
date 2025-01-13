termos = int(input('Quantos termos você quer mostrar?: '))
a = 0
b = 1
c = a + b
i = 0
print(a, end= ' ')
print(b, end= ' ')
while i < termos - 2 :
    c = a + b
    print(c, end=' ')
    a = b
    b = c
    i += 1


    