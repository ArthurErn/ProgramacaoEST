iden = int(input('Insira o número da identificação: '))

nota1 = float(input('Insira sua primeira nota:'))
nota2 = float(input('Insira sua segunda nota: '))
nota3 = float(input('Insira sua terceira nota: '))

mediaE = round((nota1 + nota2 + nota3) / 3, 1)
mediaA = (nota1 + nota2 * 2 + nota3 * 3 + mediaE) / 7

print(f'Sua identificação: {iden}')
print(f'Notas obtidas:\nPrimeira nota: {nota1}\nSegunda nota: {nota2}\nTerceira nota: {nota3}')
print(f'Média dos exercícios: {mediaE}')

if 0 >= mediaA < 4:
    print('Média de aproveitamento: E')
elif 4 >= mediaA < 6:
    print('Média de aproveitamento: D')
elif 6 >= mediaA < 7.5:
    print('Média de aproveitamento: C')
elif 7.5 >= mediaA < 9:
    print('Média de aproveitamento: B')
elif 9 >= mediaA < 10:
    print('Média de aproveitamento: A')
