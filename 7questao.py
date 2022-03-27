import random
alunos = [random.randint(0,10) for n in range(0,20)]

aprovados = 0
reprovados = 0

for i in alunos:
    if i < 7:
        reprovados = reprovados + 1
    else:
        aprovados = aprovados + 1

print("A quantidade de alunos aprovados foi:", aprovados)
print("A quantidade de alunos reprovados foi:", reprovados)
print(alunos)