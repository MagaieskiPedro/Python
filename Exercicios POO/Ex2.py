#classe conta bancaria que armazena o numero da conta, nome do titular e seu saldo
class ContaBancária:
    #construtor
    def __init__(self,numeroConta,nomeTitular,saldo):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    #metodo para realizar deposito na conta informada
    def deposito(self,numeroConta):
        if numeroConta == self.numeroConta:
            saldo += float(input("Digite quanto deseja adicionar: "))
            return saldo
        else:
            print("Numero de conta incorreto")
            return 0
    #metodo para sacar a partir da conta informada
    def saque(self,numeroConta):
        if numeroConta == self.numeroConta:
            saldo -= float(input("Digite quanto deseja sacar: "))
            return saldo
        else:
            print("Numero de conta incorreto")
            return 0