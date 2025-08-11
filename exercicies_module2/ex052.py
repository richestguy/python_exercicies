n = int(input('Digite um numero:'))


def detector(n):
    count = 0
    for c in range(1, n + 1):
        if n % c == 0:
            print('\033[33m', end='')
            count += 1
        else:
            print('\033[31m', end='')

        print(c)
    if count == 2:
        print('Primo')
    else:
        print('not primo')

detector(n)