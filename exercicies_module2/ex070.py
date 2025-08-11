primeiro = True
total = 0
more = 0
while True:
    nome = input('Digite o nome do produto:')
    preco = float(input('Digite o preco do produto:'))
    continuar = input('Deseja continuar? [S/N]').upper().strip()[0]
    if preco > 1000:
        more += 1
    if primeiro:
        menor = [nome, preco]
        primeiro = False
    elif preco < menor[1]:
        menor = [nome, preco]

    total += preco
    if continuar != 'S':
        break
print(f'{total} Total da compra. {menor[1]} Menor valor. {more}')