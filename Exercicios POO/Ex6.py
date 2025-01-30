class Produto:
    def __init__(self,nome,preco,quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade
    def valorEstoque(self):
        return self.quantidade
    def disponibilidade(self,nomeProcurado):
        if nomeProcurado == self.nome:
            return "Disponivel"
        else:
            return "Indisponivel"