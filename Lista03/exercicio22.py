# Faca um programa que leia as medias finais de varios alunos de uma turma
# e mostre a maior media, a menor media e a media aritmetica da turma.
# O programa para quando encontrar uma media negativa.

notas = []
contador = 1

while contador != 0:
    notas.append(float(input('Insira uma nota: ')))
    contador += 1
    
    resp = input('Deseja saber o resultado? S/Y?: ')
    mediaNotas = sum(notas) / len(notas)
    
    if resp == 's':
        print('=' * 80)
        print(f'A média aritmetica da turma é: {mediaNotas}')
        print(f'A maior nota da turma é: {max(notas)}')
        print(f'A menor nota da turma é: {min(notas)}')
        print('=' * 80)
    elif resp == 'n':
        continue
    
    if mediaNotas < 0:
        print('=' * 80)
        print(f'==== PROGRAMA FINALIZADO ====')
        print('=' * 80)
        break        
    

   