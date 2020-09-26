# Um determinado material radioativo perde metade de sua massa a cada
# 50 segundos. Dada a massa inicial, em gramas, fazer um programa que
# calcule o tempo necessario para que essa massa se torne menor que 0,5 grama 
# O programa em C deve escrever a massa inicial, a massa final e o tempo calculado em horas, minutos e segundos.


print("-" * 30)

print(f"{'Material Radioativo':^30}")

print("-" * 30)

massa = float(input("Massa inicial (g): "))

seg = 0

while massa >= 0.5:
    massa /= 2
    seg += 50

print("_" * 30)

print(f"A massa final = {massa:.3f}g")
minutos = 0

horas = 0

while seg >= 60:
    seg -= 60
    minutos += 1
    
    if minutos >= 60:
        
        while minutos >= 60:
            minutos -= 60
            horas += 1

print(f"Tempo = {horas}h {minutos}min {seg}s")