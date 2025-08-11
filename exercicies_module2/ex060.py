n = int(input('Digite um numero para calcular seu fatorial:'))
fatorial = 1
print('Calculando {}! = '.format(n), end='')
while n != 0:
    fatorial = fatorial * n
    n = n - 1
print('{}'.format(fatorial))
