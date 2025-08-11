s1 = float(input('Primeiro segmento: '))
s2 = float(input('Segundo segmento: '))
s3 = float(input('Terceiro segmento: '))
if s1 + s2 > s3 and s2 + s3 > s1 and s1 + s3 > s2:
    print('Segmentos formam um triangulo, e ele é:')
    if s1 == s2 and s1 == s3:
        print('Equilatero')
    elif s1 != s2 != s3 != s1:
        print('escaleno')
    else:
        print('isosceles')
else:
    print('Segmentos não formam triangulo.')