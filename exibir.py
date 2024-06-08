def exibir_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    for idx, tarefas in enumerate(tarefas):
        status = "concluída" if tarefas["concluida"] else "pendente"
        print(f"\nTarefa {idx + 1}.")
        print(f"Título: {tarefas['titulo']}")
        print(f"Descrição: {tarefas['descricao']}")
        print("Status: {}". format(status))


