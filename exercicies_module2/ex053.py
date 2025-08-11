frase = str(input('Digite uma frase: ')).strip().upper()
plavras = frase.split()
junto = ''.join(plavras)
inverso = ''
for letras in range(len(junto)-1, -1, -1):
    inverso += junto[letras]
if inverso == junto:
    print('Palindromo')
else:
    print('Else palindromo')