class Tarefa:
    def __init__(self, id, descricao, completa=False):
        self.id = id
        self.descricao = descricao
        self.completa = completa

tarefas = []

def add_tarefa(descricao):
    id = len(tarefas) + 1
    nova_tarefa = Tarefa(id, descricao)
    tarefas.append(nova_tarefa)

def excluir_tarefa(id):
    global tarefas
    tarefas = [tarefa for tarefa in tarefas if tarefa.id != id]

def exibir_tarefas():
    return tarefas

def procurar_tarefa_por_id(id):
    for tarefa in tarefas:
        if tarefa.id == id:
            return tarefa
    return None