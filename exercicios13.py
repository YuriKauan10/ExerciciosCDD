
alunos = []
acimaMedia = 0

for i in range(1,6):
    qntd = float(input(f"nota do aluno {i}: "))
    alunos.append(qntd)

soma = 0

for i in alunos:
    soma += i

calculoMedia = soma / 5

for i in alunos:
    if i > calculoMedia:
        acimaMedia += 1

print(f"A média da turma foi {calculoMedia}.")
print(f"Quantidade de alunos acima da média: {acimaMedia}")