nomeHosp = input('Insira seu nome: ')
diaria = int(input('Insira o número de diárias: '))

calcDiaria = diaria * 300

if diaria < 15:
    print(f'Olá {nomeHosp}, o total a pagar é: R${calcDiaria + 20}')
elif diaria == 15:
    print(f'Olá {nomeHosp}, o total a pagar é: R${calcDiaria + 14}')
elif diaria > 15:
    print(f'Ola {nomeHosp}, o total a pagar é: R${calcDiaria + 12}')

# Hotel
# R$300 por diaria e mais uma taxa adicional de serviços
# Se a diária for menor que 15, taxa de R$20
# Se o número de diárias for igual a 15, taxa de R$14
# Se o número de diárias for maior que 15, taxa de R$12

# Cada pessoa tem um registro com nome e total de diárias

# Imprimir o nome e o total a pagar do hóspede
