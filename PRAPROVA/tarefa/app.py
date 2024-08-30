from flask import Flask
from controllers import todo_bp  # Importa o blueprint corretamente

app = Flask(__name__)

# Registro do Blueprint
app.register_blueprint(todo_bp, url_prefix='/tarefas')  # Adiciona um prefixo para as rotas do blueprint

if __name__ == "__main__":
    app.run(debug=True)