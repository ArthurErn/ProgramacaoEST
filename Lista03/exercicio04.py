x = int(input("Insira um número de 1 a 10: "))

for cont in range(1,11):
        print('{0} x {1} = {2}'.format(x, cont, x*cont))