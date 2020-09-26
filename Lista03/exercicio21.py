# Faca um programa que leia varios conjuntos de tres valores reais e mostre
# para cada conjunto: sua soma, seu produto e sua media. O programa para
# quando um conjunto nao entrar com seus valores em ordem crescente.

condicao = True

while condicao:
    
    n1 = float(input('Insira um número: '))
    n2 = float(input('Insira um número: '))
    n3 = float(input('Insira um número: '))
    media = (n1 + n2 + n3) / 3
        
    if n1 < n2 < n3:
        print(f'A soma é: {n1 + n2 + n3}')
        print(f'O produto é: {n1 * n2 * n3}')
        print(f'A média é: {media}')
    else:
        print('===== Programa finalizado =====')
        break       