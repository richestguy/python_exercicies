payday = float(input('Digite o valor do salario: R$'))
aument =  int(input('Digite a porcentagem de aumento: %'))
percent = aument / 100
newpayday = payday + payday * percent
print('O funcionario que ganhava {:.2f}, com o aumento de {}% vai comecar a receber {:.2f}'.format(payday, aument, newpayday))