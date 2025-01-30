class Carro:
    def __init__(self,marca,modelo,velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    def acelerar(self):
        self.velocidade +=1
    def frear(self):
        self.velocidade -=1
    def exibirVelocidade(self):
        return self.velocidade
    