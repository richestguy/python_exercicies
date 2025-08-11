# 2m2 = 1l

largura = float(input('Largura: '))
altura = float(input('Altura: '))
area = largura * altura
print('Sua parede tem a dimensao de {}X{} e sua area é de {}m²'.format(largura, altura, area))
print('Para pintar essa parede, você precisara de {}L de tinta'.format(area/2))