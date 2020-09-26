# Elabore um algoritmo que leia um conjunto indeterminado de valores e informe , ao final, o maior e o menor
# valor lidos.
# O valor deverá ser encerrado se o usuário digitar um valor negativo ou valor 0

n = 1
maior = ''
menor = ''

while n > 0:
    valor = int(input('Insira um valor aleatório: '))

    if maior == '':
        maior = valor
    else:
        if maior < valor:
            maior = valor

    if menor == '':
        menor = valor
    else:
        if menor > valor:
            menor = valor

    n = int(input('Deseja continuar?: '))

    if n == "0":
        break
    else:
        print(f'Número maior: {maior}\nNúmero menor: {menor}')

        continue
