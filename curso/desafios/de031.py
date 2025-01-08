dist = int(input('Qual a distancia da viagem?: '))
if dist <= 200:
    preco = float(dist * 0.50)
    print('Sua viagem tem {} km de distancia, sua passagem é de {:.2f} reais'.format(
        dist, preco))
else:
    preco = float(dist * 0.45)
    print('Sua viagem tem {} km de distancia, sua passagem é de {:.2f} reais'.format(
        dist, preco))
