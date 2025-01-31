from math import sqrt
#classe triangulo que recebe os dois lados do triangulo e sua base
class Triângulo:
    #construtor
    def __init__(self,lado1,lado2,base):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
    #metodo que verifica se o triangulo é valido 
    def validar(self):
        if (self.lado1>0 and self.lado2>0 and self.base>0) and (self.lado1 == self.lado2):
            return "Valido"
        else:
            return "invalido"
    #metodo que calcula a area de um triangulo valido
    def area(self, validade):
        if validade == "Valido":
            altura = (self.lado1/2)*sqrt(3)
            return (self.base*altura)/2
        else:
            return 0
        