import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except:
    print('Site indisponível no momento')
else:
    print('Consegui acessar o site sem problemas!')