import urllib as url
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except url.error.URLError:
    print('O site pudim não está acessível no momento.')
else:
    print('Consegui acessar o site pudim com sucesso!')
