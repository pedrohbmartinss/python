casa = float(input('Qual o valor da casa?: '))
salario = float(input('Qual o seu salaro?: '))
anos = int(input('Em quantos anos irá pagar a casa?: '))
prestacao = casa/(anos*12)
if prestacao > (salario*0.3):
    print('NEGADO - A prestacao é maior que 30 por cento de seu salario.')
else:
    print('CONCEDIDO - Para pagar uma casa de {} reais, voce para prestacoes de {:.2f} por {} anos.'.format(casa, prestacao, anos))