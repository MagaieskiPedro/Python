#classe carro que registra marca, modelo e velocidade
class Carro:
    #construtor
    def __init__(self,marca,modelo,velocidade):
        self.marca = marca
        self.modelo = modelo
        self.velocidade = velocidade
    #metodo acelerar que incrementa velocidade
    def acelerar(self):
        self.velocidade +=1
    #metodo frear que decrementa a velocidade
    def frear(self):
        self.velocidade -=1
    #metodo que exibe a velocidade
    def exibirVelocidade(self):
        return self.velocidade
    