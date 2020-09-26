# Faça um algoritmo que solicite um valor para o usuario, e gere a tabuada deste valor.
# Por exemplo, se o usuario informar o valor 2 devera ser gerada a tabuada do numero 2, variando de 0 a 10.

valor = int(input('Insira um número de 1 a 10: '))
numAux = 0

print(f'Tabuada de {valor}')

print('=' * 20)

while numAux <= 10:
    print(f'{valor} X {numAux} = {numAux * valor}')

    numAux = numAux + 1
