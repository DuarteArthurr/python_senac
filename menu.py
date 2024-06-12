def exibir_menu():
    print("\n--- Menu de Contatos ---")
    print("1. Adicionar Contato")
    print("2. Visualizar Contatos")
    print("3. Atualizar Contato")
    print("4. Remover Contato")
    print("5. Sair")

    try:
        opcao = int(input("Escolha uma opção: "))
        return opcao
    except ValueError:
        print("Entrada inválida. Por favor, insira um número.")
        return 0