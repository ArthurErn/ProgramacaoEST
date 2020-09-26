anterior = 1
proxima = 1
soma = 1

for n in range(1, 31):
    print(anterior)
    soma = proxima + anterior
    anterior = proxima
    proxima = soma
