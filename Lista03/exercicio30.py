# Elabore um algoritmo para fazer a leitura de N notas de M alunos de
# uma turma. Os valores N e M devem ser solicitados ao usuario no inıcio
# do algoritmo. Exibir:
# • a media de cada aluno;
# • a media geral;
# • a maior e a menor media da turma

nota = []

print('====== Bem-vindo ao cálculo de notas ======')

while True:
    
    nota.append(float(input('Insira sua nota: ')))
    
    perg = input('Qual nota deseja saber? ou digite 0 para continuar: ')
    
    if perg == '0':
        continue
    elif perg == '1':
        mediaInd = (nota[0] + nota[1]) / 2
        print(f'Sua média individual é: {mediaInd}')
    elif perg == '2':
        mediaAll = sum(nota) / len(nota)
        print(f'A média geral é: {mediaAll}')
    elif perg == '3':
        print(f'A maior média da turma é: {max(notas)}')
        print(f'A menor média da turma é: {min(notas)}')
    elif perg == '4':
        mediaInd = (nota[0] + nota[1]) / 2
        mediaAll = sum(nota) / len(nota)
        print(f'Sua média individual é: {mediaInd}')
        print(f'A média geral é: {mediaAll}')
        print(f'A maior média da turma é: {max(nota)}')
        print(f'A menor média da turma é: {min(nota)}')
        

        
    
    