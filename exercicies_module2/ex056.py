media = 0
m20 = 0
maiorn = ''
maior = 0
for c in range(1, 5):
    print('-' * 5, '{} PESSOA'.format(c), '-' * 5)
    nome = input('Digite o nome:').strip()
    idade = int(input('Digite a idade:'))
    sexo = input('Digite o sexo: M/F').upper()
    if sexo == 'F' and idade < 20:
        m20 += 1
    media = (idade + media)
    if sexo == 'M':
        if c == 1:
            maiorn = nome
            maior = idade
        else:
            if idade > maior:
                maiorn = nome
                maior = idade

print(maiorn)
media = media / 4
print(media)
print(m20)