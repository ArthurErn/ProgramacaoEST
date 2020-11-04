def verificacaoIP(lista):
    cont = 0
    blocoInteiro = ''
    for item in lista:
        if item < 0 or item > 255:
            cont += 0
        else:
            cont += 1
        blocoInteiro += str(item)
        if cont != 4:
            blocoInteiro += '.'
    if cont == 4:
        print("-" * 30)
        print(f"O IP {blocoInteiro} é válido!")
    else:
        print(f"IP {blocoInteiro} é inválido!")


print("-" * 30)
print(f"{'VERICADOR DE IPv4':^30}")
print("-" * 30)

lista = []
for c in range(1, 4 + 1):
    ip = int(input("%2dº bloco: " % c))
    lista.append(ip)
verificacaoIP(lista)

    