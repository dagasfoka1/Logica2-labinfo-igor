from flask import Blueprint, render_template, request, redirect, url_for
from models import add_tarefa, excluir_tarefa, exibir_tarefas, procurar_tarefa_por_id

todo_bp = Blueprint('todo', __name__)

@todo_bp.route('/')
def index():
    tarefas = exibir_tarefas()  # Usa a função exibir_tarefas para obter a lista de tarefas
    return render_template('index.html', tarefas=tarefas)

@todo_bp.route('/adicionar', methods=['POST'])
def adicionar():
    descricao = request.form.get('descricao')
    add_tarefa(descricao)
    return redirect(url_for('todo.index'))

@todo_bp.route('/excluir/<int:id>')
def excluir(id):
    excluir_tarefa(id)
    return redirect(url_for('todo.index'))

@todo_bp.route('/completar/<int:id>')
def completar(id):
    tarefa = procurar_tarefa_por_id(id)
    if tarefa:
        tarefa.completa = True
    return redirect(url_for('todo.index'))
