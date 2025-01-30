#classe pai de onde as outras vão derivar
class Carro:
    def __init__(self, cor, velocidade):
        self.cor = cor
        self.velocidade = velocidade
    def acelerar(self):
        print(self.velocidade+1)
    def frear(self):
        print(self.velocidade-1)
#clase corvette implementa o metodo acelerar de forma diferente de um carro tradicional(classe pai)
class Corvette(Carro):
    def __init__(self,cor,velocidade):
        super().__init__(cor,velocidade)
    def acelerar(self):
        print(self.velocidade+20)

carro = Corvette("azul",50)
carro.acelerar()
