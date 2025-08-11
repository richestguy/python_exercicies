p = float(input('Digite o preco do produto: R$'))
d = int(input('Digite a porcentagem do desconto'))
percent = d / 100
discount = p - (p * percent)
print('O produto que custava {} com o desconto de {}% agora vai custar {:.2f}'.format(p, d, discount))
