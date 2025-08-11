n = int(input('Digite um numero: '))
continuar = True
count = 1
media = 0
soma = n
maior = menor = n
while continuar:
    continuar = str(input('Deseja continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        continuar = True
        n = int(input('Digite um numero: '))
        count += 1
        soma += n
        if n > maior:
            maior = n
        elif n < menor:
            menor = n
    else:
        continuar = False
        media = soma / count
        print(media, 'media')
        print(maior, 'maior', menor, 'menor')
        print(count, 'numeros digitados')