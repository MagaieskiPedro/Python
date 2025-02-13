import random as rd
class JogoAdvinhacao:
    #construtor
    def __init__(self,numeroInformado):
        self.numeroInformado = numeroInformado
        self.NumeroAleatorio = 0
    #gera um numero aleatorio na instancia da classe
    def GerarAleatorio(self):
        self.NumeroAleatorio = rd.randint(1,10)
    #Checa se o numero informado é igual ou maior/menor ao gerado
    def Checar(self):
        if self.NumeroAleatorio > self.numeroInformado:
            return "É maior que o numero informado"
        elif self.NumeroAleatorio < self.numeroInformado:
            return "É menor que o numero informado"
        else:
            return f"Acertou! {self.numeroInformado} é igual a {self.NumeroAleatorio}"
