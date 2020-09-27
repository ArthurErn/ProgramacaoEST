# Faca um programa que solicita ao usuario uma quantidade indeterminada de numeros inteiros.
# O programa deve calcular e escrever a media aritmetica apenas dos numeros pares.
# A entrada de dados deve ser encerrada quando o numero 0 (ZERO) for digitado.

contador = 1
soma = 0

while contador:
    num = int(input('Insira sua nota: '))
    
    if num == 0:
        break
        
    if num % 2 == 0:
        contador += 1
        soma += num
        
    print(f'Media Aritmetica: {soma / contador}')
