#Classe produto que recebe o nome, preco e quantidade do produto
class Produto:
    #construtor
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    #metodo que informa valor do estoque
    def valorEstoque(self):
        return self.quantidade
    #metodo que informa se o produto informado esta disponivel
    def disponibilidade(self,nomeProcurado):
        if nomeProcurado == self.nome:
            return "Disponivel"
        else:
            return "Indisponivel"