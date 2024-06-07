def calcular_media(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in alunos:
        media = (aluno['nota1'] + aluno['nota2']) / 2
        if media >= 7:
            situacao = 'Aprovado'
        elif 5 <= media < 7:
            situacao = 'Recuperação'
        else:
            situacao = 'Reprovado'

        print(f"Aluno: {aluno['nome']}")
        print(f"Media: {media:.2f}")
        print(f"Situacao: {situacao}")
