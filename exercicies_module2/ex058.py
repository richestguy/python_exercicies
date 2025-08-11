from random import randint

r= randint(0,10)
print(r)
print('Acabei de pensar em um numero entre 0 e 10\n Sera que voce consegue adivinhar qual foi?')
guess = int(input('Qual seu palpite?'))
tentativas = 0
while guess != r:
    print('Tente novamente')
    guess = int(input('Qual seu palpite?'))
    tentativas += 1
tentativas += 1
print('Voce acertou com {} tentativas'.format(tentativas))




