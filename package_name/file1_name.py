# Testar a acessibilidade ao Youtube

import urllib
import urllib.request

url = str(input("Informe o url do site:")).strip()

try:
    site = urllib.request.urlopen(url)
except  urllib.error.URLError:
    print('O site não está acessível no momento.')
else:
    print('Consegui acessar o site com sucesso!')
    print(site.read())
