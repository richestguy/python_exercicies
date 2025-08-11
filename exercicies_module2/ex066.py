n = soma = count = 0
while True:
    n = int(input('Digite um valor: '))
    if n == 999:
        break
    soma += n
    count += 1
print(f'A soma destes {count} valores vale: {soma}')