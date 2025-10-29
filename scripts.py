"""Encapsulation"""

# class BadBankAccount:
#     def __init__(self, balance: float):
#         self.balance = balance


# account = BadBankAccount(0.0)
# account.balance = -1
# print(account.balance)


class BankAccount:
    def __init__(self):
        self._balance = 0.0

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount: float):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")

        self._balance += amount

    def withdraw(self, amount: float):
        if amount <= 0:
            raise ValueError("Withdraw amount must be positive")
        if amount > self._balance:
            raise ValueError("Insufficient funds")

        self._balance -= amount


account1 = BankAccount()
print(account1.balance)
account1.deposit(1.99)
print(account1.balance)
account1.withdraw(1)
print(account1.balance)
account1.withdraw(100)
print(account1.balance)
