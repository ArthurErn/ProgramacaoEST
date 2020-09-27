cont = n = soma = 0

while n <= 10:
    n = int(input('Digite um número: '))
    soma += n
    cont += 1
    if cont == 10:
        break


print('No total, foram {} números digitados e a soma entre eles é {}.'.format(cont, soma))

