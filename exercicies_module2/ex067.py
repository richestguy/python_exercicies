n = count = 1
while True:
    n = float(input('Digite um numero para ver sua tabuada:'))
    if '-' in str(n):
        break
    while count < 11:
        print(f'{n} x {count} = {n*count}')
        count += 1
    count = 0
print('Numero negativo indentificado parando programa.')