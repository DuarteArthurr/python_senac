class Tarefa:
    def __init__(self, id, titulo, descricao):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.status = 'Pendente'

    def __str__(self):
        return f"ID: {self.id}\nTítulo: {self.titulo}\nDescrição: {self.descricao}\nStatus: {self.status}\n"

    def atualizar_status(self, novo_status):
        self.status = novo_status
