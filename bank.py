class BalanceException(Exception):
    pass

class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"\nAccount '{self.name}' created. \n Balance = ${self.balance:.2f}")


    def get_balance(self):
        print(f"\nAccount '{self.name} balance = ${self.balance:.2f}")


    def deposit(self, amount):
        self.balance = self.balance + amount 
        print(f"\n Deposit complete. \nAccount '{self.name} balance = ${self.balance:.2f}")
        self.get_balance()

    def viableTransaction(self,amount):
        if self.balance >= amount:
            return 
        else:
            raise BalanceException(
                f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}"
            )
        
    def withdraw(self,amount):
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount 
            print("\nWithdraw complete. ")
            self.get_balance()
        except BalanceException as Error:
            print(f"\nWithdraw interrupted:{Error}")


    def transfer(self, amount, account):
        try:
            print("\n****************\n \nBeginning Transfer...")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete \n**********************")
        except BalanceException as Error:
            print(f"\nTransfer failed")