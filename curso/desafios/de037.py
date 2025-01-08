numero = int(input('Digite um numero: '))
print("""1 - Binário
2 - Octal
3 - Hexadecimal""")
opcao = int(input('Escolha uma opção:'))
if opcao == 1:
    print('{} convertido em numero binario é {}'.format(numero,bin(numero)))
elif opcao == 2:
    print('{} convertido em numero octal é {}'.format(numero,oct(numero)))
else:
    print('{} convertido em numero hexadecimal é {}'.format(numero,hex(numero)))