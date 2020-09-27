n = int(input('Digite um valor: '))
soma = 0

for divisor in range(1, n):
    if n % divisor == 0:
        soma += divisor

if n == soma:
    print(f'O número {n} é perfeito!')
else:
    print(f'O número {n} não é perfeito!')