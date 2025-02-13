import operator
#classe loja virtual que recebe uma lista de produtos e uma lista dos precos dos mesmos
class LojaVirtual:
    #construtor
    def __init__(self,produtos:list = ["Livro"],precos:list= [5]):
        self.produtos = produtos
        self.precos = precos
    #metodo que cadastra um produto e seu preco
    def cadastrarProduto(self,produto,preco):
        self.produtos.append(produto)
        self.precos.append(preco)
    #metodo que lista os itens e seus respectivos produtos
    def gerarCarrinho(self):
        carrinho = dict(zip(self.produtos,self.precos))
        return carrinho
    #metodo que aplica o desconto aos itens do carrinho
    def aplicarDesconto(self,desconto):
        k = [desconto] * len(self.precos)
        self.precos = list(map(operator.sub, self.precos, k))
        print(self.precos)
    #metodo que calcula o total da compra
    def calcularTotal(self):
        print(f"a soma da compra eh: {sum(self.precos):.2f}")
#implementacao da classe
lojinha = LojaVirtual(["carrinho"],[1])
lojinha.cadastrarProduto("Carro",10)
lojinha.aplicarDesconto(0.2)
carrinho =  lojinha.gerarCarrinho()
lojinha.calcularTotal()
print(carrinho)