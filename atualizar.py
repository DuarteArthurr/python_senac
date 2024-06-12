def atualizar_contato(contatos):
    try:
        nome = input("Digite o nome do contato a ser atualizado: ")

        for contato in contatos:
            if contato['nome'] == nome:
                telefone = input("Digite o novo telefone: ")
                email = input("Digite o novo email: ")

                contato['telefone'] = telefone
                contato['email'] = email

                print("Contato atualizado com sucesso!")
                return

        print("Contato não encontrado.")

    except Exception as e:
        print(f"Ocorreu um erro ao atualizar o contato: {e}")