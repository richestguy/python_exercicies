from datetime import datetime

born = int(input('Digite o ano de nascimento: '))
sex = str(input('Digite o sexo: [M/F]: ')).upper()

now = datetime.now().year
idade = now - born
if sex == 'M':
    print('Quem nasceu em {} no ano de {} tem {} anos.'.format(born, now, idade))
    if idade < 18:
        remaining = 18 - idade
        print('Faltam {} anos para o alistamento'.format(remaining))
        print('Seu alistamento será em {}'.format(now + remaining))
    elif idade > 18:
        remaining = idade - 18
        print('Você ja deveria ter se alistado ha {} anos'.format(remaining))
        print('Seu alistamento foi em {}'.format(now - remaining))
    else:
        print('Você tem que se alistar imediatamente!')
else:
    print('Você não pode se alistar!')