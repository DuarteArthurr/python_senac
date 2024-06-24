from tarefa import Tarefa


class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1

    def adicionar_tarefa(self, titulo, descricao):
        tarefa = Tarefa(self.proximo_id, titulo, descricao)
        self.tarefas.append(tarefa)
        self.proximo_id += 1

    def visualizar_tarefas(self):
        return self.tarefas

    def localizar_tarefa(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None

    def atualizar_tarefa(self, id, novo_status):
        tarefa = self.localizar_tarefa(id)
        if tarefa:
            tarefa.atualizar_status(novo_status)
            return True
        return False

    def remover_tarefa(self, id):
        tarefa = self.localizar_tarefa(id)
        if tarefa:
            self.tarefas.remove(tarefa)
            return True
        return False
