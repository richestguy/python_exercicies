rent = int(input('Quandos dias alugados:'))
kilometer = int(input('Quantos kilometros:'))
total = kilometer * 0.15 + rent * 60
print('O total a pagar é de R${:.2f}'.format(total))