lista = []
for i in range(3):
    newNum = int(input('Insira um número: '))
    lista.append(newNum)
print(sorted(lista, reverse=True))