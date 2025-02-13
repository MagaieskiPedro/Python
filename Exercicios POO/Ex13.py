#classe agenda que lista os nomes e seus telefones
class Agenda:
    #construtor
    def __init__(self,nome:list=[],numTelef:list=[]):
        self.nome = nome
        self.numTelef = numTelef
    #metodo que adiciona registro na agenda
    def adicionar(self,nome,numTelef):
        self.nome.append(nome)
        self.numTelef.append(numTelef)
    #metodo que edita registro na agenda
    def editar(self,nome=None,numTelf=None):
        if nome in self.nome or numTelf in self.numTelef:
            indice = self.nome.index(nome)
            self.nome[indice] = nome
            self.numTelef[indice] = numTelf
            print(self.nome,self.numTelef)
    #metodo que remove um registro da agenda
    def remover(self,nome,numTelf):
        self.nome.remove(nome)
        self.numTelef.remove(numTelf)
#implementação da classe
agenda = Agenda(["carlos","alberto"],[1,4])
agenda.editar("alberto",3)

