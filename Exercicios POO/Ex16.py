class RedeSocial:
    def __init__(self,nome,mensagem):
        self.nome = nome
        self.mensagem = mensagem
    def adicionarAmigos(self,nome):
        if self.buscarUsuarios(nome):
            return f"Amigo {nome} adicionado"
        else:
            return f"Amigo {nome} não encontrado"
    def publicarMensagem(self):
        return self.mensagem
    def buscarUsuarios(self,nome):
        if nome == self.nome:
            return True
        else:
            return False
    def comentarEmPost(self,comentario):
        return f"A mensagem {self.mensagem} possui o comentario: {comentario}"