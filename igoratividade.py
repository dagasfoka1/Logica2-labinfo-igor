def Media(pessoa):
    return (pessoa["materia1"][1]+ pessoa["materia2"][1] +pessoa["materia3"][1])/3
def exibir(p1):
    return p1
def set(pessoa,id):
    med=Media(pessoa)
    pessoa.media=med
p1=[{
    "id":1,
    "nome":"igor",
    "idade":"20 anos",
    "prontuario": "Sp12345",
    "materia1":["portugues",6],
    "materia2":["matematica", 8],
    "materia3":["ciencias",10],
    "media": 0
},
{
    "id":2,
    "nome":"ana",
    "idade":"19 anos",
    "prontuario": "Sp12345",
    "materia1":["portugues",3],
    "materia2":["matematica", 10],
    "materia3":["ciencias",9],
    "media": 0
}]
class pessoa:
    def __init__(self,id,nome,idade,prontuario,materia1,materia2,materia3,media):
        self.id=id
        self.nome=nome
        self.idade=idade
        self.prontuario=prontuario
        self.materia1=materia1    
        self.materia2=materia2 
        self.materia3=materia3
        self.media=media     
def add():
    nova_pessoa=pessoa()#8inputs e fazer função pra calcular media
    nova_pessoa["id"]=p1[-1]["id"] +1 if p1 else 1
    p1.append(nova_pessoa)
    return jsonify(nova_pessoa),201

print(p1[0])