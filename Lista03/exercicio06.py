total = 1
num = ''

while num != 0:
    
    num = int(input("Digite um número: "))
    
    if num == 0:
        break
        
    total *= num
    
    print(f"O resultado dos produtos é: {total}")