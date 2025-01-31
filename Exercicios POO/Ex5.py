#classe funcionario que recebe nome salario e cargo
class Funcionário:
    #construtor
    def __init__(self,nome,salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    #metodo que calcula salario liquido com o imposto sendo informado
    def calcularSalarioLiq(self,porcImposto):
        self.salario = self.salario-(self.salario*porcImposto)
        return self.salario