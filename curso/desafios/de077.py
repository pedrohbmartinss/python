palavras = ('APRENDER', 'PROGRAMAR', 'LINGUAGEM',
            'PYTHON', 'CURSO', 'GRATIS', 'ESTUDAR', 
            'PRATICAR', 'TRABALHAR', 'MERCADO', 'PROGRAMADOR',
            'FUTURO')
for i in palavras:
    print(f'\nNa palavra {i} temos ', end='')
    for letra in i:
        if letra in 'AEIOU':
            print(f'{letra}', end=' ')