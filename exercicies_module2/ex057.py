sexo = str(input('Digite seu sexo: [M/F] ')).upper().strip()[0]
while sexo not in 'MF':
    sexo = str(input('Dados invalidos por favor tente novamente:')).upper().strip()
print('Sexo {} definido!'.format(sexo))