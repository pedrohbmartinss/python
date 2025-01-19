i = 0
s = 0
while True:
    n = int(input('Digite um numero: '))
    if n == 999:
        break
    i += 1
    s += n
print(f'Foram digitados {i} numeros e a soma deles foi {s}')