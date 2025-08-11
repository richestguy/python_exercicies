from _datetime import datetime

countm = 0
count = 0
now = datetime.now().year

for n in range(1,8):
    year = int(input('Digite o ano de nascimento: '))
    if now - year >= 18:
        countm += 1
    else:
        count += 1
print('maiore {} menores{}'.format(countm, count))