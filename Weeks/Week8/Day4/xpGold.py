class BankAccount:
    balance = 0
    def __init__(self,minimum_balance=0):
        self.minimum_balance = minimum_balance
        
    def deposit(self,deposit):
        self.deposit = deposit
        if self.deposit >= 0:
            BankAccount.balance += self.deposit
        else:
            print("The amount must be positive, bye bye")
    
    def withdraw(self,withdraw):
        self.withdraw = withdraw
        if self.withdraw >= 0:
            BankAccount.balance -= self.withdraw
        else:
            print(f"The amount must be positive, bye bye")

class MinimumBalanceAccount(BankAccount):
    def withdraw(self,withdraw):
        self.withdraw = withdraw
        if self.withdraw - BankAccount.balance > self.minimum_balance:
            BankAccount.withdraw(self.withdraw)
        else:
             print(f"You can not withdraw more than your current balance of {BankAccount.balance}, bye bye")

            
deposit_1 = MinimumBalanceAccount()
deposit_1.deposit(50)
withdraw_1 = MinimumBalanceAccount()
withdraw_1.withdraw(10)
print(BankAccount.balance)