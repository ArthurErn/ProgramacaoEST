# 1 - Soma
# 2 - Produto
# 3 - Divisão
# 4 - Potência

condicao = True

while condicao:
    num1 = float(input('Digite um número: '))
    num2 = float(input('Digite um número: '))

    if num1 == 0 or num2 == 0:
        break

    calculo = int(input('Qual operação deseja fazer?: '))

    if calculo == 1:
       soma = num1 + num2
       print(soma)
    elif calculo == 2:
        multi = num1 * num2
        print(multi)
    elif calculo == 3:
        divi = num1 / num2
        print(divi)
    elif calculo == 4:
        poten = num1 ** num2
        print(poten)
