class Peao:
    #construtor da classe peao (é um peão branco apenas) inicializado na segunda linha da segunda coluna
    def __init__(self,x=2,y=2,):
        self.x =x
        self.y = y
        self.ocupado = True
    #metodo mover que define se é o movimento inicial(2 casas) ou de apenas 1 casa para frente
    def mover(self,deslocamento):
        if y==2 and deslocamento==2:
            self.y = self.y + 2
        elif deslocamento==1:
            self.y = self.y + 1
        else:
            print("Deslocamento incorreto")
    #checa se há outra instancia de um peão nas casas da direita ou esquerda
    def checarOcupado(self):
        if self.x+1 and self.ocupado ==True:
            return "Esquerda"
        elif self.x-1 and self.ocupado == True:
            return "Direita"
        return "Reto"
    #se houver um peão a direita ou esquerda na casa 5(moveu duas casas), pode ser realizado o enPassant para traz desse peão
    def enPassant(self,deslocamento):
        if self.y==5 and deslocamento==1:
            if self.checarOcupado() == "Direita":
                self.y+1
                self.x-1
            elif self.checarOcupado() == "Esquerda":
                self.y+1
                self.x+1
            else:
                self.mover(deslocamento)
class Torre:
    #construtor da classe torre inicializado na linha 1 e coluna 1
    def __init__(self,x=1,y=1):
        self.x = x
        self.y = y
    def mover(self,x,y,deslocamento):
        if deslocamento >0:
            if 8-x > 0 and 8-y >0:
                self.x += x
                self.y += y
            else:
                print("Deslocamento incorreto")
        elif deslocamento < 0:
            if 8+x < 0 and 8+y <0:
                self.x += x
                self.y += y
            else:
                print("Deslocamento incorreto")
        else:
            print("Deslocamento incorreto")