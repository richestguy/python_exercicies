vel = float(input('Qual a velocidade atual? '))
if vel > 80:
    print('Voce foi multado em exatamente R${}'.format((vel - 80)*7))
else:
    print('Voce esta dentro do limite!')
print('Tenha um bom dia! Dirija com segurança!')