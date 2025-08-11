year = sex = m18 = m20 = h = 0
while True:
    year = int(input('Digite a idade:'))
    sex = str(input('Digite o sexo: [M/F]')).upper().strip()[0]
    continuar = str(input('Quer continuar? [S/N]')).upper().strip()[0]
    if continuar == 'S':
        if year > 18:
            m18 += 1
        if sex == 'M':
            h += 1
        if sex == 'F' and year < 20:
            m20 += 1
    else:
        if year > 18:
            m18 += 1
        if sex == 'M':
            h += 1
        if sex == 'F' and year < 20:
            m20 += 1
        break
print(f'''{m18} pessoas com mais de 18 anos.
{h} homens cadastrados.
{m20} mulheres com menos de 20 anos.''')