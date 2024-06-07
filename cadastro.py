
def cadastrar_aluno(alunos):
    nome = input('Digite o nome do aluno: ')
    idade = input('Digite o idade do aluno: ')
    cidade = input('Digite o cidade do aluno: ')
    nota1 = float(input('Digite a primeira nota do aluno: '))
    nota2 = float(input('Digite a segunda nota do aluno: '))
    aluno = {
        'nome': nome,
        'idade': idade,
        'cidade': cidade,
        'nota1': nota1,
        'nota2': nota2,
    }
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")
