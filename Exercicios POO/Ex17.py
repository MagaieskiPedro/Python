class Biblioteca:
    def __init__(self,nome = "",autor = ""):
        self.nome = nome
        self.autor = autor
        self.disponivel = True
    def cadastrarLivro(self,nome,autor):
        self.nome = nome
        self.autor = autor
        self.disponivel = True
    def emprestar(self,nome):
        if self.nome == nome and self.disponivel ==True:
            self.disponivel = False
            return f"O livro {nome} foi emprestado"
        else:
            return f"O livro {nome} esta indisponivel"
    def devolver(self,nome):
        if self.nome == nome and self.disponivel ==False:
            self.disponivel = True
            return f"O livro {nome} foi devolvido"
        else:
            return f"O livro {nome} já está aqui"
    def disponibilidade(self,nome):
        if self.nome == nome and self.disponivel ==True:
            return f"O livro {nome} esta disponivel"
        else:
            return f"O livro {nome} foi emprestado"