distance = float(input('Qual a distancia da sua viagem: KM'))
if distance <= 200:
    cust = distance * 0.50
    print('Sua viagem custa R${:.2f}'.format(cust))
else:
    cust = distance * 0.45
    print('Sua viagem custa R${:.2f}'.format(cust))
print('Tenha um bom dia!')