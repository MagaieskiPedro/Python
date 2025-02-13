from math import pow
#Classe circulo que calcula perimetro e raio a partir do parametro raio
class Círculo:
    #construtor
    def __init__(self,raio):
        self.raio = raio
    #metodo perimetro calcula perimetro a partir de raio multiplicado por 2 e pi
    def perimetro(self):
        return 2*self.raio*3.14
    #metodo area que calcula area a partir da potencia do raio multiplicada pela constante pi
    def area(self):
        return pow(self.raio,2)*3.14