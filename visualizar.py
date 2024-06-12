def visualizar_contatos(contatos):
    if not contatos:
        print("Nenhum contato encontrado.")
        return

    for i, contato in enumerate(contatos, start=1):
        print(f"\nContato {i}:")
        print(f"Nome: {contato['nome']}")
        print(f"Telefone: {contato['telefone']}")
        print(f"Email: {contato['email']}")