# Chico tem 1.50m / Cresce 2cm por ano
# Zé tem 1.10m / Cresce 3cm por ano
# Quantos anos são necessarios para que Zé seja maior que Chico?

chico = 150
ze = 110
anos = 0

while chico >= ze:
    anos = anos + 1
    chico = chico + 2
    ze = ze + 3

    print(f'Altura de Chico: {chico}cm')
    print(f'Altura de Zé: {ze}cm')
    print(f'Será necessário {anos} anos para Zé ficar maior do que Chico')
