from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    desenvolvedor = request.form['desenvolvedor']
    turma = request.form['turma']
    professor = request.form['professor']
    data = request.form['data']
    nota = request.form['nota']
    confianca = request.form['confianca']

    return render_template('result.html', desenvolvedor=desenvolvedor, turma=turma, professor=professor, data=data, nota=nota, confianca=confianca)

if __name__ == '__main__':
    app.run(debug=True)