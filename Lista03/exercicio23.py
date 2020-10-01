# Faca um programa que leia um numero n e mostre na tela os n primeiros
# numeros pares e depois os n primeiros numeros ımpares

num = []
contador = 1

while True:
    num.append(int(input("Digite um número: ")))
    contador += 1
    
    perg = input("Deseja imprimir os números?: ")
    
    if perg == 's':
        print('==== Primeiros números pares ====')
        
        for valor in num:
            if valor % 2 == 0:
                print(valor)
        
        print('==== Primeiros números ímpares ====')
        
        for valor in num:
            if not valor % 2 == 0:
                print(valor)

    elif perg == 'n':
        continue
    elif perg == 'sair':
        break
    else:
        print('==== Inválido ====')
        continue
    
    
    
    
    