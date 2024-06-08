def excluir_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas cadastradas")
        return

    try:
        indice = int(input("Digite o numero da tarefa que deseja excluir: ")) - 1
        if indice <= 0 < len(tarefas):
            tarefa_excluida = tarefas.pop(indice)
            print(f"Tarefa '{tarefa_excluida ['titulo']}' excluida com sucesso!")
        else:
            print("Número da tarefa inválido.")
    except ValueError:
        print("Entrada invalida. por favor, digite um numero.")