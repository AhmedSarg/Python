class Bank:
    def __init__(self):
        self.balance = 0
        print("Welcome to Deposit & Withdrawal Machine!")
    
    def deposit(self, cash):
        self.balance = self.balance + cash
        print("Amount Deposited:", cash)

    def withdraw(self, cash):
        if cash <= self.balance:
            self.balance -= cash
            print("You withdraw:", cash)
            print("Net Available Balance=", self.balance)
        else:
            print("Not Enough Balance")


account = Bank()
account.deposit(15000)
account.withdraw(5000)
account.withdraw(5000)
account.withdraw(10000)
