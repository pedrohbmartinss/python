opcao = ''
i = soma = media = 0
maior = 0
menor = 999999999999999999999999999999
while opcao != 'n':
    n = int(input('Digite um número: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    i += 1
    soma += n
    opcao = input('Voce quer continuar?(S/N)').lower()
media = soma/i
print('Você digitou {} numeros e a media foi {}'.format(i, media))
print('O maior valor foi {} e o menor foi {}'.format(maior, menor))