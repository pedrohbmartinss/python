resposta = input('Digite algo: ')
print('O tipo primitivo desse valor e: ', type(resposta))
print('Só tem espaços?:', resposta.isspace() )
print('É numerico?:', resposta.isnumeric() )
print('É alfabetico?:', resposta.isalpha() )
print('É alfanumerico?:', resposta.isalnum() )
print('Esta em maiuscula?:', resposta.isupper() )
print('esta em minuscula?:', resposta.islower() )
