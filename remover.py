def remover_contato(contatos):
    try:
        nome = input("Digite o nome do contato a ser removido: ")

        for contato in contatos:
            if contato['nome'] == nome:
                contatos.remove(contato)
                print("Contato removido com sucesso!")
                return

        print("Contato não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao remover o contato: {e}")