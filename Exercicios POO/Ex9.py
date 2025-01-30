class Paciente:
    def __init__(self,nome,idade,historico:list):
        self.nome = nome
        self.idade = idade
        self.historico = historico
    def addConsulta(self,consulta):
        self.historico.append(consulta)
    def exibirConsultas(self):
        return self.historico