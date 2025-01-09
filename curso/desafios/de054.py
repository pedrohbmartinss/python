import datetime
maior = 0
menor = 0
atual = datetime.date.today().year
for i in range(0,7):
    ano = int(input('Em que ano nasceu a {}º pessoa: '.format(i+1)))
    if atual - ano < 21:
        menor += 1
    else:
        maior += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maior))
print('Ao todo tivemos {} pessoas menores de idade'.format(menor))
