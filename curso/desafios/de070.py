soma = float(0)
caro = int(0)
menor = 99999
prodbarato = ' '
while True:
    produto = input('Nome do produto: ')
    preco = int(input('Preço R$: '))
    soma += preco
    if preco > 1000:
        caro += 1
    if preco < menor:
        menor = preco
        prodbarato = produto
    opcao = input('Quer continuar?: [S/N] ').upper()
    if opcao == 'N':
        break
print('-'*20, 'Fim do programa', '-'*20)
print(f'O total da compra foi R${soma}')
print(f'Temos {caro} produtos custando mais de R$ 1000.00')
print(f'O produto mais barato foi {prodbarato} que custa {menor} reais.')

