sexo = input('Insira seu sexo: ')
altura = float(input('Insira sua altura: '))

if sexo == "Homem":
    mC = round((72.7 * altura) - 58, 1)
    print(f'Seu peso ideal é {mC}kg')
elif sexo == "Mulher":
    wC = round((62.1 * altura) - 44.7, 1)
    print(f'Seu peso ideal é {wC}kg')
else:
    print('Inválido')
