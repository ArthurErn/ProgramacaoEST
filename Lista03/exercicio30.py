# Elabore um algoritmo para fazer a leitura de N notas de M alunos de
# uma turma. Os valores N e M devem ser solicitados ao usuario no inıcio
# do algoritmo. Exibir:
# • a media de cada aluno;
# • a media geral;
# • a maior e a menor media da turma

alunos = int(input("Digite a quantidade de alunos na sala: "))
provas = int(input("Digite a quantidade de provas aplicadas: "))

maiorNota = ''
alunoMaiorNota = ''

menorNota = ''
alunoMenorNota = ''

somaNotas = 0
notaGeral = []

for aluno in range(alunos):
  
  nomeAluno = str(input("Digite o nome do aluno: "))

  notas = 0

  for nota in range(notas):
    nota = float(input("Digite a nota da prova: "))
    notas += notas
  
  media = notas / provas

  if(maiorNota == ''):
    maiorNota = media
    maiorNotaAluno = nomeAluno
  elif(media > maiorNota):
    maiorNota = media
    maiorNotaAluno = nomeAluno
  if(menorNota == ''):
    menorNota = media
    menorNotaAluno = nomeAluno
  elif(media < menorNota):
    menorNota = media
    menorNotaAluno = nomeAluno

  print(f"{nomeAluno} nota final: {round(media, 2)}")
  notaGeral.append(media)
  somaNotas += media

print("Média de todos os alunos: ", notaGeral)

print(f"Maior média: {maiorNotaAluno}, {maiorNota}")
print(f"Menor média: {alunoMenorNota}, {menorNota}")

mediaGeralAluno = somaNotas / alunos

print(f"A média final da turma foi: {round(mediaGeralAluno, 2)}")
