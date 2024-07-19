class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade
    def GetNome(self):
        return self.__nome

class Professor(Pessoa):
    def __init__(self, nome, idade, materia):
        super().__init__(nome, idade)
        self.__materia = materia

class Nota:
    def __init__(self, prova, trabalho):
        self.__prova = prova
        self.__trabalho = trabalho
        self.__media= 0
    def GetMedia(self):
        self.__media= (self.__prova + self.__trabalho)/2
        return self.__media 

class Materia:
    def __init__(self, nome):
        self.__nome = nome
    def GetMateria(self):
        return self.__nome

class Aluno(Pessoa):
    def __init__(self, nome, idade, prontuario, nota,materia):
        super().__init__(nome, idade)
        self.__prontuario = prontuario
        self.__nota = nota
        self.__materia = materia.GetMateria()
        self.__notas=[]
    def Add_nota(self):
        media = self.__nota.GetMedia()
        self.__notas.append(media) 
    def Apresentar(self):
        for nota in self.__notas:
            print(f"O aluno {self.GetNome()} de prontuário {self.__prontuario} na matéria  {self.__materia} ficou com a média {self.__notas}")
