x = int(input('Insira um valor: '))
y = int(input('Insira um valor: '))
z = int(input('Insira um valor: '))

if x < 0 and y < 0 and z < 0:
    print('Os valores não podem formar um triângulo')
elif x == y and x == z and y == z:
    print('O triângulo é Equilátero')
elif x == y and x != z:
    print('O triângulo é Isóceles')
elif x == z and y != z:
    print('O triângulo é Isóceles')
elif x != y and x != z and y != z:
    print('O triângulo é Escaleno')
