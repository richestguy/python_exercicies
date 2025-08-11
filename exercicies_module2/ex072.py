valor = int(input("Qual valor você quer sacar? R$ "))
total = valor
ced = 50
totced = 0

print('=' * 40)
print(f"Saque solicitado: R$ {valor}")
print('=' * 40)

while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"Total de {totced} cédula(s) de R$ {ced}")
        # passa para a próxima cédula
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break

print('=' * 40)
print("VOLTE SEMPRE!")
print('=' * 40)
