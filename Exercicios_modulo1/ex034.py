payday = float(input('Qual é o salario do funcionario?'))
if payday > 1250.00:
    newpayday = payday * 0.1 + payday
    print('Quem ganhava {} passa a ganhar {:.2f}'.format(payday, newpayday))
elif payday <= 1250.00:
    newpayday = payday * 0.15 + payday
    print('Quem ganhava {} passa a ganhar {:.2f}'.format(payday, newpayday))
print('Valeu cz!')