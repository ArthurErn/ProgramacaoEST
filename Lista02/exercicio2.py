nome = input('Insira seu nome: ')
sexo = input('Insira seu sexo: ')
estadoCivil = input('Insira seu estado civil: ')

if sexo == "F" and estadoCivil == "CASADA":
    casaTemp = int(input('Insira seu tempo de casamento: '))
    print(f'Olá {nome}, seu gênero é {sexo}, {estadoCivil} e tem {casaTemp} anos de casamento')
else:
    print(f'Olá {nome}, seu gênero {sexo}, {estadoCivil}')
