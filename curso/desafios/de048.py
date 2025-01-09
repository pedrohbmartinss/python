soma = 0
valores = 0
for i in range(1,501):
    if i % 2 > 0:
        if i % 3 ==0:
            print(i)
            soma += i
            valores += 1
print(soma)
print(valores)
            
