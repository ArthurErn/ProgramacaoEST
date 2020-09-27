valor = int(input('Insira um valor: '))
modoPaga = input('Insira o método de pagamento: ')

vistaDC = valor - (valor * 10 / 100)
cartaoCreditoV = valor - (valor * 15 / 100)
etiquetaCJ = valor + (valor * 10 / 100)

if modoPaga == 'Dinheiro' or modoPaga == 'Cheque':
    print(f'Método de pagamento: {modoPaga}')
    print(f'O valor a pagar com desconto de 10% é R${vistaDC}')
elif modoPaga == "Crédito":
    print(f'Método de pagamento: {modoPaga}')
    print(f'O valor a pagar com desconto de 15% é R${cartaoCreditoV}')
elif modoPaga == 'Dinheiro, parcelado':
    print(f'Método de pagamento: {modoPaga}')
    print(f'Pagamento em 2 parcelas de R${valor}')
elif modoPaga == "Crédito, parcelado":
    print(f'Método de pagamento: {modoPaga}')
    print(f'Pagamento de 2 parcelas de R${etiquetaCJ}')

# valor + (valor * 15 / 100)

# À vista em dinheiro ou cheque, recebe 10% de desconto
# À vista no cartão de crédito, recebe 15% de desconto
# Em duas vezes, preço normal de etiqueta sem juros
# Em duas vezes, preço normal de etiqueta mais juros de 10%

# Elabore um algoritmo que calcule o que deve ser pago por um produto,
# considerando o preço normal de etiqueta e a escolha da condição de paga-
# mento. Utilize os códigos da tabela a seguir para ler qual a condição de
# pagamento escolhida e efetuar o cálculo adequado.
