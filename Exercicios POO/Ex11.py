#Classe banco que recebe o nome do cliente, numero da sua conta e seu saldo
class Banco:
    #construtor
    def __init__(self,nome='',numConta=123,saldo=50.5):
        self.nome = nome
        self.numConta = numConta
        self.saldo = saldo
    #metodo que cadastra um cliente pelo nome
    def cadastrarCliente(self,nome):
        self.nome = nome
        print(f"Cliente {self.nome} cadastrado")
    #metodo que cria uma conta no nome de um cliente cadastrado
    def abrirConta(self,numConta,nome):
        if nome == self.nome:
            self.numConta = numConta
            print(f"Conta {self.numConta} criada")
    #metodo que saca o dinheiro de uma conta informada
    def saque(self,numConta):
        if numConta == self.numConta:
           while True:
            print(f"Seu saldo é {self.saldo}")
            saque = float(input("Digite quanto deseja sacar:"))
            if saque <= self.saldo:
                 self.saldo -= saque
                 return saque
            else:
                tentativa = input("Voce não tem esse dinheiro, digite [S] para sair ou outra coisa para continuar ")
                if tentativa == "S":
                    break
    #metodo que deposita certo dinheiro informado em uma conta informada
    def deposito(self,numConta,dinheiro):
        if numConta != None:
            self.saldo +=dinheiro
            print(f"Deposito de {dinheiro} reais foi realizado com sucesso")
        else: 
            print(f"Deposito de {dinheiro} reais NÃO foi realizado com sucesso")
    #metodo que deposita certo dinheiro informado em uma conta informada
    def transferencia(self,dinheiro,numConta):
        if numConta != None:
            self.saldo +=dinheiro
        else:
            print("Conta inexistente")
#demonstracao da classe em funcionamento
banco = Banco()
# banco.abrirConta()
banco.cadastrarCliente("Carlos")
# saque = banco.saque(123)
# print(f"o saque de {saque} foi realizado")
banco.deposito(123,200)