"""Stactic Method vrs Instance Method"""


class BankAccount:

    MIN_BALANCE = 100

    def __init__(self, owner, balance=0):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.MIN_BALANCE += amount
            print(f"{self.owner}'s new balance is ${self.MIN_BALANCE}")
        else:
            print("Enter a value greater than 0")


    def withdraw(self, amount):
        if amount > 0:
            self.MIN_BALANCE -= amount
            print(f"{self.owner}'s new balance is ${self.MIN_BALANCE}")
        else:
            print("Enter a value greater than 0")
    
    @staticmethod        
    def is_valid_interest_rate(rate):
        return  0 <= rate <= 5
            
            
account1 = BankAccount("Yaw", 500)
account1.deposit(200)
account1.withdraw(76)
print(BankAccount.is_valid_interest_rate(10))
print(BankAccount.is_valid_interest_rate(4))