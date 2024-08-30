from model import User
from flask import Flask,Blueprint,render_template,redirect,request,url_for
app=Flask(__name__)

main=Blueprint("main",__name__)

@main.route("/")
def index():
    return render_template("index.html")
@main.route("/result",methods=['POST'])
def result():
    user=User(request.form["nome"],request.form["email"],request.form["senha"])
    return redirect(url_for('tarefas.index'),nome=user.nome,email=user.email,senha=user.senha)
app.register_blueprint(main)
if __name__ == '__main__':
    app.run(debug=True)