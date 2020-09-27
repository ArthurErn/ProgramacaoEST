peso = float(input('Insira seu peso: '))
altura = float(input('Insira sua altura: '))

formIMC = round(peso / (altura * altura), 1)

if 0 > formIMC < 18.5:
    print(f'Seu IMC é {formIMC}, você está abaixo do peso!')
elif 18.5 >= formIMC < 24.9:
    print(f'Seu IMC é {formIMC}, você está com peso normal!')
elif 25 >= formIMC < 29.9:
    print(f'Seu IMC é {formIMC}, você está acima do peso!')
elif formIMC >= 30:
    print(f'Seu IMC é {formIMC}, você está obeso!')
