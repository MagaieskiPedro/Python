#Classe retangulo que calcula perimetro e area a partir da altura e largura
class Retângulo:
    #construtor
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    #metodo que calcula o perimetro a partir dos dados no construtor
    def perimetro(self):
        return self.largura*2+self.altura*2
    #metodo que calcula area a partir dos dados do construtor
    def area(self):
        return self.largura*self.altura