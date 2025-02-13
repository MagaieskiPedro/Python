#classe maquina de vendas que recebe listas dos produtos, precos e quantidade em estoque
class maquinaDeVendas:
    #construtor
    def __init__(self,produtos:list = [],precos:list =[],quantidadeEstoq:list =[]):
        self.produtos = produtos
        self.precos = precos
        self.quantidadeEstoq = quantidadeEstoq
    #metodo que cadastra um novo produto
    def cadastrarProd(self,nome,preco,quantidadeEstoq):
        self.nome.append(nome)
        self.preco.append(preco)
        self.quantidade.append(quantidadeEstoq)
    #metodo que seleciona um produto informado
    def selecionarProd(self,nome):
        indice = self.produtos.index(nome)
        print(self.produtos[indice])
        print(self.precos[indice])
        print(self.quantidadeEstoq[indice])
    #metodo que insere dinheiro, escolhe a quantidade e nome do produto
    def inserirDinheiro(self,nome,pagamento,quantidade):
        if nome in self.produtos:
            indice = self.produtos.index(nome)
            if quantidade*self.precos[indice] >pagamento and self.quantidadeEstoq[indice] >quantidade:
                troco =  quantidade*self.precos[indice] - quantidade*pagamento
                print(f"O seu troco é: {troco}")
                return troco
            else:
                print("Dinheiro insuficiente")
    #metodo que consulta o estoque do produto
    def consultarEstoque(self,nome):
        indice = self.produtos.index(nome)
        estoque = self.quantidadeEstoq[indice]
        print(f"O estoque do produto é: {estoque}")
#implementação da classe
maquininha = maquinaDeVendas(["Prod"],[3.14],[5])
maquininha.selecionarProd("Prod")
#aqui esta pagando 3 itens por 2 (total de 6), como custa 3.14(*3 = 9.42), fica 9.42-6 = 3.42 de troco
maquininha.inserirDinheiro("Prod",2,3)