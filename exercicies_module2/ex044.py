print('|{}|Loja|{}|'.format('='*5, '='*5))
price = int(input('Digite o valor do produto: '))
print('''[1] a vista dinheiro/cheque.
[2] a vista no cartão.
[3] em até 2x no cartão
[4] 3x ou mais no cartão.''')
option = int(input('Escolha sua opção:'))

if option == 1:
    newprice = price - price * 0.1
    diferenca = price - newprice
    print('Já que você vai pagar a vista o preço final será {} com a diferença de {} do preço original'.format(newprice, diferenca))
elif option == 2:
    newprice = price - price * 0.05
    diferenca = price - newprice
    print('Já que o pagamento é a vista o preço final sera {} com a diferença de {} do preço original'.format(newprice, diferenca))
elif option == 3:
    parcela = price /2
    print('Parcelando o produto em 2x o valor da parcela será de {} e o valor do produto será {}'.format(parcela, price))
else:
    times = int(input('Quantas parcelas?'))
    if times <= 2:
        print('Quantidade de parcelas invalida.')
    else:
        newprice = price + price * 0.2
        parcela =  newprice / times
        acrecimo = newprice - price
        print('Parcelando o produto em {}x o valor da parcela será de {} com um acrescimo de {}, totalizando um valor final de {}'.format(times, parcela, acrecimo, newprice))
