#classe paciente que recebe nome, idade e uma lista com historico de consultas do paciente
class Paciente:
    #construtor
    def __init__(self,nome,idade,historico:list):
        self.nome = nome
        self.idade = idade
        self.historico = historico
    #metodo que adiciona uma consulta a lista do historico do paciente
    def addConsulta(self,consulta):
        self.historico.append(consulta)
    #metodo que exibe as consultas do paciente
    def exibirConsultas(self):
        return self.historico