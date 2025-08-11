
n = int(input('Digite um numero inteiro:'))

print('Escolha uma das opções:')
print('[ 1 ] converter para BINARIO')
print('[ 2 ] converter para OCTAL')
print('[ 3 ] converter para HEXADECIMAL')

option = int(input('Sua escolha: '))

if option == 1:
    nw = bin(n)[2:]
    print('{} convertido para BINARIO é igual a {}'.format(n, nw))
elif option == 2:
    nw = oct(n)[2:]
    print('{} convertido para OCTAL é igual a {}'.format(n, nw))
elif option == 3:
    nw = hex(n)[2:]
    print('{} convertido para HEXADECIMAL è igual a {}'.format(n, nw))
else:
    print('Opção não existe!')
