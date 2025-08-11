#imports
from datetime import date
from calendar import isleap
#input
ano = int(input('Que ano quer analisar? Coloque 0 para analisar o ano atual:'))
#year verify
if ano == 0:
    ano = date.today().year
    verify = isleap(ano)
else:
    verify = isleap(ano)
# bissex verify
if verify:
    print('O ano {} é bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))