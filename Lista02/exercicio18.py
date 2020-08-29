salarioB = float(input('Insira seu salário bruto: '))
valorP = float(input('Insira o valor da prestação: '))

calcEmpr = salarioB - (salarioB * 30 / 100)

if valorP > calcEmpr:
    print(f'O valor não pode ser concedido\nLimite de 30% do salário bruto')

# A prefeitura de São José da Serra abriu uma linha de crédito para os
# funcionários estatutários. O valor máximo da prestação não poderá ultra-
# passar 30% do salário bruto. Fazer um algoritmo que permita entrar com
# o salário bruto e o valor da prestação, e informar se o empréstimo pode ou
# não ser concedido
