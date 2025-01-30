#classe pai de onde as outras vão derivar
class Carro:
    def __init__(self, cor, velocidade):
        self.cor = cor
        self.velocidade = velocidade
    def acelerar(self):
        print(self.velocidade+1)
    def frear(self):
        print(self.velocidade-1)
#classe Marrea recebe o atributo velocidade herdado da classe pai Carro
class Marea(Carro):
    def __init__(self,cor,velocidade):
        super().__init__(cor,velocidade)
    def explodir(self):
        if self.idade>1 and self.velocidade>20:
            print("Explodiu")
        else:
            print("Vai explodir futuramente")
#classe Uno recebe o atributo velocidade herdado da classe pai Carro
class Uno(Carro):
    def __init__(self,cor,velocidade,acessorio):
        super().__init__(cor,velocidade)
        self.acessorio = acessorio
    def AdentrarHiperespaco(self):
        if self.acessorio == "Escada" or "Adesivo Empresa":
            self.velocidade = 3E8
            print(self.velocidade)
        else:
            print("Ainda não alcançou seu potencial")

carro = Uno("branco", 5,"Escada")
carro.AdentrarHiperespaco()