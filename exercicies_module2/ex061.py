print('Gerador de PA')
print('=-=' * 10)
p1 = float(input('Primeiro termo: '))
r = float(input('Razao: '))
p = 0
c = 0
while c != 10:
    p = p1 + (c) * r
    c += 1
    print(p, end=' > ')
print('FIM')
