numerador = 1
denominador = 1
resultado = 0

print(f'Inicio = {numerador} / {denominador}')

for i in range(1, 50):
    numerador += 2
    denominador += 1

    print(numerador, '/', denominador)
