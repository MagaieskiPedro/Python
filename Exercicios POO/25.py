class Personagem:
    def __init__(self,saude,forca,defesa,habilidade,pocoes=3):
        self.saude = saude
        self.vida = self.saude
        self.forca = forca
        self.defesa = defesa
        self.habilidade = habilidade
        self.pocoes = pocoes
        self.ativado = False
    def levelUp(self):
        while True:
            escolha = input("Escolha um atributo para aprimorar: Saude Forca Defesa \n")
            escolha = escolha.title()
            match escolha:
                case "Saude":
                    self.saude += 5
                    break
                case "Forca":
                    self.forca += 1
                    break
                case "Defesa":
                    self.defesa +=10
                    break
                case _:
                    print("Atributo incorreto!")
    def atacar(self):
        if self.habilidade == "Furia" and self.ativado == True:
            print("Furia barbaro")
            ataque = self.forca*2.5
            self.ativado = False
        else:
            ataque = self.forca*0.9
        print(f"O ataque é {ataque}")
        return ataque
    def defender(self,ataque):
        if self.habilidade == "Escudo Invencivel" and self.ativado == True:
            self.vida = self.vida -(ataque-self.defesa*2)
            self.ativado = False
        else:
            self.vida = self.vida - (ataque-self.defesa*0.45)
        print(f"A saude maxima é {self.saude}")
        print(f"A vida atual é {self.vida}")
    def ativarHabilidade(self):
        self.ativado = True
    def usarPocao(self):
        if self.vida+10 < self.saude:
            self.vida += 10
            self.pocoes -= 1
        else:
            self.vida = self.saude
            self.pocoes -= 1
        print(f"A vida restante é {self.vida}")
        print()
    def checarVitoria(self):
        if self.vida <0:
            return f"Perdeu, vida chegou a {self.vida}"
        else:
            return f"A vida chegou a {self.vida}"
            
paladino = Personagem(50,25,50,"Escudo Invencivel")
barbaro = Personagem(30,60,10,"Furia")
barbaro.ativarHabilidade()
ataque = barbaro.atacar()
paladino.ativarHabilidade()
paladino.defender(ataque)
print(paladino.checarVitoria())
paladino.usarPocao()
paladino.levelUp()