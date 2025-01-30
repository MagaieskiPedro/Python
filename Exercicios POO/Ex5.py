class Funcionário:
    def __init__(self,nome,salario,cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo
    def calcularSalarioLiq(self,porcImposto):
        self.salario = self.salario-(self.salario*porcImposto)
        return self.salario