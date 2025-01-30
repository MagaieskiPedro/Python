from math import sqrt
class Triângulo:
    def __init__(self,lado1,lado2,base):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
    def validar(self):
        if (self.lado1>0 and self.lado2>0 and self.base>0) and (self.lado1 == self.lado2):
            return "Valido"
        else:
            return "invalido"
    def area(self, validade):
        if validade == "Valido":
            altura = (self.lado1/2)*sqrt(3)
            return (self.base*altura)/2
        else:
            return 0
        