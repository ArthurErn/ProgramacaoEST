# Faca um programa que leia varios inteiros positivos e mostre, no final, a
# soma dos numeros pares e a soma dos numeros ımpares. O programa para
# quando entrar um numero maior que 1000.

condicao = True

somaPar = 0
somaImpar = 0

while condicao:

    numero = int(input('Digite um número inteiro: '))

    if numero % 2 == 0 and numero >= 0:
        somaPar += numero
    elif numero < 0:
        print('Esse número não é permitido')
        break
    elif numero > 1000:
        print('Esse número não é permitido!')
        break
    else:
        somaImpar += numero

    print(f'A soma dos números pares é {somaPar}')
    print(f'A soma dos números ímpares é {somaImpar}')
