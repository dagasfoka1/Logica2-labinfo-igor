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
        self.__media = 0
    
    def GetMedia(self):
        self.__media = (self.__prova + self.__trabalho) / 2
        return self.__media 

class Materia:
    def __init__(self, nome):
        self.__nome = nome
    
    def GetMateria(self):
        return self.__nome

class Aluno(Pessoa):
    def __init__(self, nome, idade, prontuario, notas, materia):
        super().__init__(nome, idade)
        self.__prontuario = prontuario
        self.__notas = [Nota(nota[0], nota[1]) for nota in notas]  # Lista de objetos Nota
        self.__materia = materia.GetMateria()
        self.__medias = []
    
    def Add_nota(self):
        for nota in self.__notas:
            media = nota.GetMedia()
            self.__medias.append(media)
    
    def Apresentar(self):
        print(f"O aluno {self.GetNome()} de prontuário {self.__prontuario} na matéria {self.__materia} ficou com as seguintes médias:")
        print(f"Média: {}")

# Exemplo de uso
matematica = Materia("Matemática")
notas_aluno = [[8.0, 7.5], [7.5, 8.0]]  # Exemplo de duas notas para o aluno
aluno = Aluno("Maria", 20, "54321", notas_aluno, matematica)
aluno.Add_nota()
aluno.Apresentar()