x = int(input('Insira um número: '))
y = int(input('Insira um número: '))
z = int(input('Insira um número: '))

if x < y < z:
    print(z, y, x)
elif x > y > z:
    print(x, y, z)
elif y > z > x:
    print(y, z, x)
elif z > x > y:
    print(z, x, y)
elif x < y > z:
    print(y, x, z)
elif x > y < z:
    print(y, x, z)
