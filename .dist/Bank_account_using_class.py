class Account:
    def __init__(self,name,account_number,balance):
        self.name=name
        self.account_number=account_number
        self.balance=balance

    def Deposite(self,Money):
        self.balance +=Money

    def Withdraw(self,Money):
        self.balance -=Money 


    def Balance(self):
        print(f'\nTotal Amount of {self.name} is :{self.balance}')



Bank=Account('kishan',12321,1200)
Bank.Deposite(5000)
Bank.Balance()