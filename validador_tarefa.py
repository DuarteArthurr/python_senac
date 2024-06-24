def validar_id(id):
    try:
        id = int(id)
        if id > 0:
            return id
        else:
            raise ValueError
    except ValueError:
        print("ID inválido. Deve ser um número inteiro positivo.")
        return None

def validar_status(status):
    if status.lower() in ['pendente', 'concluída']:
        return status.capitalize()
    else:
        print("Status inválido. Use 'Pendente' ou 'Concluída'.")
        return None
