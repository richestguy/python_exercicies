from colors1 import colors
#visual
print(colors.terminalGreen('='*34))
print(colors.terminalYellow('Sistema de aprovação de emprestimo'))
print(colors.terminalGreen('='*34))
#inputs

homevalue = float(input(colors.terminalBold('Valor da casa: R$')))
payday = float(input(colors.terminalBold('Valor da renda: R$')))
years = int(input(colors.terminalBold('Quantos anos de financiamento? ')))

#visual
print(colors.terminalRed('='*34))
print('Analisando proposta')
print(colors.terminalRed('='*34))

#system
""" p nao pode ser maior que maxp """
p = homevalue / (years * 12)
maxp = payday * 0.3

if p > maxp:
    print(colors.terminalCyan('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(homevalue, years, p)))
    print('Emprestimo', colors.terminalRed('NEGADO!'))
else:
    print(colors.terminalCyan('Para pagar uma casa de R${:.2f} em {} anos a prestação será de R${:.2f}.'.format(homevalue, years, p)))
    print('Emprestimo', colors.terminalGreen('AUTORIZADO!'))
print(colors.terminalGreen('='*34))

