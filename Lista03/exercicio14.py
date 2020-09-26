# Faca um programa que solicita ao usuario um numero real positivo.
# Verifique se o numero e realmente positivo
# e em caso contrario solicite ao usuario digitar novamente
# (este processo pode se repetir inumeras vezes e chamado de consistencia,
# pois garante que o numero sera valido apos a entrada de dados)

# Saidas
# Pedido ao usuario = “Digite um numero real positivo”
# Caso numero valido = “O numero digitado e valido”
# Caso numero invalido = “Numero invalido, tente novamente”

condicao = True

while condicao:
    numReal = float(input('Digite um número real positivo: '))

    if numReal >= 0.0:
        print('O número inserido é valido')
        condicao = False
    else:
        print('Numero Inválido, tente novamente!')
        continue
