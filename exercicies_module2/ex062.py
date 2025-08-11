print('Gerador de PA')
print('=-='*10)

p1 = int(input('Primeiro termo: '))
r = int(input('Razao: '))
p = 0 # RESULTADO DA PA
mais = 10
total = 0
c = 0

while mais != 0:
    total = total + mais
    while c != total:
        p = p1 + c * r
        print('{}'.format(p), end=' > ')
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos voce quer mostrar a mais?'))

print('FIM')
print('=-='*10)
print('Foram mostradas {} termos '.format(total))
