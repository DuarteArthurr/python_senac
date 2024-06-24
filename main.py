from gerenciador_tarefas import GerenciadorTarefas
from validador_tarefa import validar_id, validar_status
from menu import mostrar_menu, obter_opcao


def main():
    gerenciador = GerenciadorTarefas()

    while True:
        mostrar_menu()
        opcao = obter_opcao()

        if opcao == '1':
            titulo = input("Digite o título da tarefa: ")
            descricao = input("Digite a descrição da tarefa: ")
            gerenciador.adicionar_tarefa(titulo, descricao)
            print("Tarefa adicionada com sucesso!")

        elif opcao == '2':
            tarefas = gerenciador.visualizar_tarefas()
            if tarefas:
                for tarefa in tarefas:
                    print(tarefa)
            else:
                print("Nenhuma tarefa cadastrada.")

        elif opcao == '3':
            id = validar_id(input("Digite o ID da tarefa: "))
            if id is not None:
                tarefa = gerenciador.localizar_tarefa(id)
                if tarefa:
                    print(tarefa)
                else:
                    print("Tarefa não encontrada.")

        elif opcao == '4':
            id = validar_id(input("Digite o ID da tarefa: "))
            if id is not None:
                novo_status = validar_status(input("Digite o novo status (Pendente/Concluída): "))
                if novo_status:
                    if gerenciador.atualizar_tarefa(id, novo_status):
                        print("Status da tarefa atualizado com sucesso!")
                    else:
                        print("Tarefa não encontrada.")

        elif opcao == '5':
            id = validar_id(input("Digite o ID da tarefa: "))
            if id is not None:
                if gerenciador.remover_tarefa(id):
                    print("Tarefa removida com sucesso!")
                else:
                    print("Tarefa não encontrada.")

        elif opcao == '6':
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    main()
