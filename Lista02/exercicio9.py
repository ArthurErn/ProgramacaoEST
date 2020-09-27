A = int(input('Insira um valor para A: '))
B = int(input('Insira um valor para B: '))
C = int(input('Insira um valor para C: '))
D = int(input('Insira um valor para D: '))

if B > A:
    A = B
if C > A:
    A = C
if D > A:
    A = D

print(f'Maior: {A}')

if B < A:
    A = B
if C < A:
    A = C
if D < A:
    A = D

print(f'Menor: {A}')

# Construa um algoritmo que, dado quatro valores A, B, C e D, imprima
# em tela o maior e o menor valor
