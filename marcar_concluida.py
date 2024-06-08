def marcar_tarefa_concluida(tarefas):
    if not tarefas:
        print('Não há tarefas cadastradas')
        return tarefas

    try:
        indice = int(input('Informe o numero da tarefa que deseja marcar como concluida: ')) - 1
        if 0 <= indice < len(tarefas):
            tarefas[indice]["concluida"] = True
            print('Tarefa marcada com sucesso')
        else:
            print("Numero da tarefa invalido.")
    except ValueError:
        print('Numero invalido. Por favor digite um numero.')
