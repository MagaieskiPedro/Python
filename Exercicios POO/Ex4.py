#Classe aluno que armazena o nome, matricula e as notas em uma lista
class Aluno: 
    #construtor
    def __init__(self,nome,matricula,notas:list):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    #metodo que adiciona uma nota a lista de notas do aluno
    def adicionarNota(self,nota):
        self.notas.append(nota)
    #metodo que calcula a media final do aluno a partir da lista de notas
    def calcularNotas(self):
        soma = sum(self.notas)
        tamanho = len(self.notas)
        final = soma/tamanho
        self.notas = final
        return final
    #metodo que devolve a situacao do aluno a partir da media informada
    def situacao(self,media):
        if media >5:
            return "Aprovado"
        else:
            return "Reprovado"
#demonstracao do funcionamento da classe
aluno = Aluno("carlos","123",[6,6])
aluno.adicionarNota(4)
media = aluno.calcularNotas()
situacao = aluno.situacao(media)
print(media," ", situacao)
