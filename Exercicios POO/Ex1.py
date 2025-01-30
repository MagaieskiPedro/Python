from math import pow
class Círculo:
    def __init__(self,raio):
        self.raio = raio
    def perimetro(self):
        return 2*self.raio*3.14
    def area(self):
        return pow(self.raio,2)*3.14