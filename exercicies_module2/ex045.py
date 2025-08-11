#visual
from random import randint


print('Suas opções:')
print('''[1] PEDRA
[2] PAPEL
[3] TESOURA''')
#input
option = int(input('Qual é sua jogada?'))-1
print('JO')
print('KEN')
print('PO')
print('-' * 20)
#system
pcoption = randint(0, 2)
stroptions = ('PEDRA', 'PAPEL', 'TESOURA')


if option <=2:

    if option == pcoption:
        print('Computador jogou {}'.format(stroptions[pcoption]))
        print('Voce jogou {}'.format(stroptions[option]))
        win = 'EMPATE'
        print('-' * 20)
        print(win)
    elif option == 0 and pcoption == 2:
        print('Computador jogou {}'.format(stroptions[pcoption]))
        print('Voce jogou {}'.format(stroptions[option]))
        win = 'JOGADOR VENCE'
        print('-' * 20)
        print(win)
    elif option == 1 and pcoption == 0:
        print('Computador jogou {}'.format(stroptions[pcoption]))
        print('Voce jogou {}'.format(stroptions[option]))
        win = 'JOGADOR VENCE'
        print('-' * 20)
        print(win)
    elif option == 2 and pcoption == 1:
        print('Computador jogou {}'.format(stroptions[pcoption]))
        print('Voce jogou {}'.format(stroptions[option]))
        win = 'JOGADOR VENCE'
        print('-' * 20)
        print(win)
    else:
        print('Computador jogou {}'.format(stroptions[pcoption]))
        print('Voce jogou {}'.format(stroptions[option]))
        win = 'COMPUTADOR VENCE'
        print('-'*20)
        print(win)
else:
    print('JOGADA INVALIDA!')
