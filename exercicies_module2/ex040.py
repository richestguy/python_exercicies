n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))

media = (n1 + n2) / 2

print('Quem tirou {} e {} tem a média {}'.format(n1, n2, media))

if 7> media >= 5:
    print('Aluno em recuperação')
elif  media < 5:
    print('Aluno REPROVADO')
else:
    print('Aluno APROVADO')