#classe jogo cartas
class JogoCartas:
    #construtor
    def __init__(self,numJogadores=0,numCartas=0):
        self.numJogadores = numJogadores
        self.numCartas = numCartas
    #metodo que embaralha
    def embaralhar():
        print("Embaralhou")
    #metodo que distribui as cartas de acordo com o numero de jogadores
    def distribuir(self):
        if self.numCartas/self.numJogadores<4:
            print("Muitos jogadores")
        else:
            self.numCartas -= self.numJogadores*4
            print("Cada jogador recebe 4 cartas")
    #metod jogar
    def jogar():
        print("Podem jogar")