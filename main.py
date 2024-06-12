from menu import exibir_menu
from adicionar import adicionar_contato
from visualizar import visualizar_contatos
from atualizar import atualizar_contato
from remover import remover_contato

def main():
    contatos = []

    while True:
        opcao = exibir_menu()

        if opcao == 1:
            adicionar_contato(contatos)
        elif opcao == 2:
            visualizar_contatos(contatos)
        elif opcao == 3:
            atualizar_contato(contatos)
        elif opcao == 4:
            remover_contato(contatos)
        elif opcao == 5:
            print("Saindo do programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()