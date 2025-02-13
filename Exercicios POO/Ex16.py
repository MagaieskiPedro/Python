class RedeSocial:
    #construtor
    def __init__(self,nome,mensagem =""):
        self.nome = nome
        self.mensagem = mensagem
    #adiciona um amigo que tenha sido instanciado como usuario na classe
    def adicionarAmigos(self,nome):
        if self.buscarUsuarios(nome):
            return f"Amigo {nome} adicionado"
        else:
            return f"Amigo {nome} não encontrado"
    #retorna a mensagem digitada 
    def publicarMensagem(self,mensagem =""):
        self.mensagem = mensagem
        return self.mensagem
    #busca um usuario digitado na instancia da classe
    def buscarUsuarios(self,nome):
        if nome == self.nome:
            return True
        else:
            return False
    #retorna a mensagem concatenada com um comentario
    def comentarEmPost(self,comentario):
        return f"A mensagem {self.mensagem} possui o comentario: {comentario}"