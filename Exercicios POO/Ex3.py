class Retângulo:
    def __init__(self,largura,altura):
        self.largura = largura
        self.altura = altura
    def perimetro(self):
        return self.largura*2+self.altura*2
    def area(self):
        return self.largura*self.altura