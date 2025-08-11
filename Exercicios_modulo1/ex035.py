print('-='*15)
print('Analisador de Tiangulos')
print('-='*15)

#inputs
s1 = float(input('Primeiro segmento:'))
s2 = float(input('Segundo segmento:'))
s3 = float(input('Terceiro segmento:'))

#verify
if s1+s2 > s3 and s2+s3 > s1 and s3+s1 > s2:
    print('Os segmentos podem formar um triangulo.')
else:
    print('Os segmentos não podem formar um triangulo.')