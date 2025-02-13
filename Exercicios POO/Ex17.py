class Biblioteca:
<<<<<<< HEAD
    #construtor
=======
>>>>>>> f1d958339cd7b6a657f41dee70a334f20c06fbaf
    def __init__(self,nome = "",autor = ""):
        self.nome = nome
        self.autor = autor
        self.disponivel = True
    #cadastra um livro na instancia da classe
    def cadastrarLivro(self,nome,autor):
        self.nome = nome
        self.autor = autor
        self.disponivel = True
    #empresta um livro disponivel e muda seu estado para indisponivel
    def emprestar(self,nome):
        if self.nome == nome and self.disponivel ==True:
            self.disponivel = False
            return f"O livro {nome} foi emprestado"
        else:
            return f"O livro {nome} esta indisponivel"
    #devolve um livro indisponivel e muda seu estado para disponivel
    def devolver(self,nome):
        if self.nome == nome and self.disponivel ==False:
            self.disponivel = True
            return f"O livro {nome} foi devolvido"
        else:
            return f"O livro {nome} já está aqui"
    #devolve o estado do livro: disponivel ou indisponivel
    def disponibilidade(self,nome):
        if self.nome == nome and self.disponivel ==True:
            return f"O livro {nome} esta disponivel"
        else:
            return f"O livro {nome} foi emprestado"