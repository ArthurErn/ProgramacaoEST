# Dois valores inteiros
# A soma dos numeros pares desse intervalo de numeros, incluindo os numeros digitados
# A multiplicacao dos numeros ımpares desse intervalo de numeros, incluindo os numeros digitados.

soma = 0
multi = 1

for contador in range(2):
    numero = int(input('Digite um número: '))
   
    if numero % 2 == 0: 
        soma += numero
    else:
        multi *= numero

print('=' * 80)
print(f'A soma dos números pares: {soma}')
print('=' * 80)
print(f'A multiplicação dos números ímpares: {multi}')
print('=' * 80)
