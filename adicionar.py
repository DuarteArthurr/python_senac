def adicionar_contato(contatos):
    try:
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")
        email = input("Digite o email: ")

        contato = {
            'nome': nome,
            'telefone': telefone,
            'email': email
        }

        contatos.append(contato)
        print("Contato adicionado com sucesso!")

    except Exception as e:
        print(f"Ocorreu um erro ao adicionar o contato: {e}")