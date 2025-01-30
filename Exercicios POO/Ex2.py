class ContaBancária:
    def __init__(self,numeroConta,nomeTitular,saldo):
        self.numeroConta = numeroConta
        self.nomeTitular = nomeTitular
        self.saldo = saldo
    def deposito(self,numeroConta):
        if numeroConta == self.numeroConta:
            saldo += float(input("Digite quanto deseja adicionar: "))
            return saldo
        else:
            print("Numero de conta incorreto")
            return 0
    def saque(self,numeroConta):
        if numeroConta == self.numeroConta:
            saldo -= float(input("Digite quanto deseja sacar: "))
            return saldo
        else:
            print("Numero de conta incorreto")
            return 0