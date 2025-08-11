from random import randint

player = int(input('Digite um numero:'))
decision = str(input('Quer escolher par ou impar? [P/I]')).upper().strip()[0]
pc = 0
count = soma  = 0

while True:
    pc = randint(0, 10)
    soma = pc + player
    if soma % 2 == 0: # numero é par ou nao
        if decision == 'P': #numero é par
            count += 1
            print(f'Voce ganhou.')
            soma = 0
            player = int(input('Digite um numero:'))
            decision = str(input('Quer escolher par ou impar? [P/I]')).upper().strip()[0]
        else:
            break
    else:
        if decision == 'I':
            count += 1
            print(f'Voce ganhou.')
            soma = 0
            player = int(input('Digite um numero:'))
            decision = str(input('Quer escolher par ou impar? [P/I]')).upper().strip()[0]
        else:
            break
print(f'Voce perdeu, mas conseguiu ganhar {count} vezes.')