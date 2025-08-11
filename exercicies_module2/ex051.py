p1 = int(input('Primeiro termo: '))
r = int(input('Razão'))
print(p1, end='>')
for c in range(0, 9):
    p1 = p1 + r
    print(p1, end='>')
print('ACABOU')
2