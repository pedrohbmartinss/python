import math
n = int(input('Deseja calcular o fatorial de qual numero?: '))
i = n
f = 1
while i != 0:
    print('{} '.format(i), end = '')
    if i > 1:
        print('X ', end= '')
    else:
        print('= ')
    f *= i 
    i -= 1
print('{}'.format(f))
