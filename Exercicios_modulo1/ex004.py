
ipt = input('Digite algo:')
print(' Numero: {} \n Letra: {} \n Alfanumerico: {} \n Maiusculo: {} \n Minusculo: {} \n Só espaços: {} \n Capitalizada: {}'.format(ipt.isnumeric(), ipt.isalpha(), ipt.isalnum(), ipt.isupper(), ipt.islower(), ipt.isspace(), ipt.istitle()))