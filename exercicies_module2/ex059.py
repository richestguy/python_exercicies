from time import sleep

n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
option = 0
while option != 5:
    print('''[1] Somar
    [2] Multiplicar
    [3] Maior
    [4] Novos numeros
    [5] Sair do programa''')
    option = int(input('Qual sua opçao?'))
    sleep(1)
    if option == 1:
        print('somando...')
        print('A soma entre {} + {} = {}'.format(n1, n2, n1 + n2))
    if option == 2:
        print('multiplicando...')
        print('{} X {} = {}'.format(n1, n2, n1 * n2))
    if option == 3:
        print('maior...')
        print('{} e {}'.format(n1 + 1, n2 +1))
    if option == 4:
        n1 = float(input('Digite um valor: '))
        n2 = float(input('Digite outro valor: '))
    else:
        print('Saindo do programa...')
        sleep(1)