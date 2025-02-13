#classe livro que recebe o titulo, autor e numero de paginas, e registra a disponibilidade do livro
class Livro:
    #construtor
    def __init__(self,titulo,autor,numeroPag):
        self.titulo = titulo
        self.autor = autor
        self.numeroPag = numeroPag
        self.disponibilidade = True
    #metodo que checa disponibilidade
    def checarDisponibilidade(self):
        if self.disponibilidade == True:
            return "Disponivel"
        else:
            return "Indisponivel"
    #metodo que empresta um livro disponivel e o marca como indisponivel
    def emprestar(self):
        if self.disponibilidade == True:
            self.disponibilidade = False
            return "Emprestado"
        else:
            return "Indisponivel para emprestimo"
    #metodo que devolve um livro indisponivel
    def devolver(self,disponibilidade):
        if disponibilidade ==  "Indisponivel":
            self.disponibilidade = True
            return "Devolvido"
        else:
            return "Livro já esta conosco, oq vc esta devolvendo?"
