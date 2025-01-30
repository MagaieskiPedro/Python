class Aluno: 
    def __init__(self,nome,matricula,notas:list):
        self.nome = nome
        self.matricula = matricula
        self.notas = notas
    def adicionarNota(self,nota):
        self.notas.append(nota)
    def calcularNotas(self):
        soma = sum(self.notas)
        tamanho = len(self.notas)
        final = soma/tamanho
        self.notas = final
        return final
    def situacao(self):
        if self.notas >5:
            return "Aprovado"
        else:
            return "Reprovado"
aluno = Aluno("carlos","123",[6,6])
aluno.adicionarNota(4)
media = aluno.calcularNotas()
situacao = aluno.situacao()
print(media," ", situacao)
