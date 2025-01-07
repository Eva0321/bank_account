from bank import *

Eva = BankAccount(1000, "Eva")
Jeff = BankAccount(1000000, "Jeff")

# Eva.get_balance()
# Jeff.get_balance()

Eva.deposit(1000)
Jeff.deposit(2000)

Eva.withdraw(50000)

Jeff.transfer(60000,Eva)