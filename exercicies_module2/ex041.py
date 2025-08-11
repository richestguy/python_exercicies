from datetime import datetime

born = int(input('Digite o ano do seu nascimento: '))

now = datetime.now().year
idade = now - born
print('Você tem {} anos portanto sua categoria é:'.format(idade))
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif 19 < idade <=25:
    print('Senior')
else:
    print('Master')