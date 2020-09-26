# Faca um programa que solicita ao usuario dois valores inteiros e positivos
# que serao a base e o expoente. O programa deve usar laco de repeticao para
# calcular e escrever o resultado da base elevado ao expoente (potencia).

base = int(input('Digite a base: '))
expoente = int(input('Digite o expoente: '))

potencia = 1
contador = 0

while contador != expoente:
    potencia = potencia * base
    contador = contador + 1

print(f'O valor de {base} elevado a {expoente} é igual a {potencia}')
