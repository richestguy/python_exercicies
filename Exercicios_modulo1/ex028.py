#imports
from random import randint

#interface
print('--'.join('='*19))
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('--'.join('='*19))
num = int(input('Em que numero eu pensei? '))

#generate number
mind = randint(0,5)

#verify and response
if num == mind:
    print('Parabens voce venceu!')
else:
    print('Numero errado tente novamente.')