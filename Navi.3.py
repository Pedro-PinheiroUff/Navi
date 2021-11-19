alunos = dict()

# Filtrando as notas dos alunos

while len(alunos) < 5:

    notas = input().replace(",", ".")

    try:

        notas = float(notas)
        if notas >0:

                alunos["aluno" + str(len(alunos)+1)] = notas
        else:
            print("Nota inválida, digite novamente.")

    except:

        print("Nota inválida, digite novamente.")

# Ordenando os alunos

ordem = sorted(alunos.items(), key=lambda x: x[1])

print(ordem[-1][0], ", ", ordem[-1][1])



