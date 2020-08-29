print("=" * 20, 'Equação do 2°grau', '=' * 20)

A = int(input('Insira um número para A: '))
B = int(input('Insira um número para B: '))
C = int(input('Insira um número para C: '))

bhas = (B * B) - 4 * A * C

print('=' * 20)

print(f'B² - 4 x A x C')
print(f'{B ** 2} - {4 * A * C}')
print(f'O resultado é: {bhas}')

# Construir um algoritmo para calcular as raı́zes de uma equação do 2 o grau,
# sendo que os valores dos coeficientes A, B, e C devem ser fornecidos pelo
# usuário através do teclado.
