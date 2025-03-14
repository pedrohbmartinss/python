
def maior(* numeros):
    maio = 0
    print('=-'* 40)
    print('Analisando os valores passados...')
    if numeros == '':
        print('Foram encontrados 0 valores ao todo.')
        print('O maior valor foi 0.')
    else:
        print(f'{numeros}', end=' ')
        print(f'foram informados {len(numeros)} valores ao todo')
        for num in numeros:
            if num > maio:
                maio = num
        print(f'O maior valor encontrado foi {maio}')





maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()