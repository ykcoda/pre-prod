"""Stactic Method"""

from datetime import datetime

from Customer import Customer


class BankAccount:

    MIN_BALANCE = 100

    def __init__(self, customer: Customer, balance: float = 0):
        self.customer = customer
        self._balance = balance
        print(f"{customer.name}'s current balance is {balance}")

    def deposit(self, amount: float):

        if not self._is_amount_valid(amount):
            print("Enter a value greater than 0")
            return

        self._balance += amount
        self._log_transaction("deposited", amount)
        print(f"{self.customer.name}'s new balance is ${self._balance}")

    def withdraw(self, amount: float):
        if not self._is_amount_valid(amount):
            print("Enter a value greater than 0")
            return

        if self._is_balance_valid(self._balance, amount):
            self._balance -= amount
            self._log_transaction("withdrawal", amount)
            print(f"{self.customer.name}'s new balance is ${self._balance}")
            return

        print("You have exceeded your minimum balance")

    @staticmethod
    def is_valid_interest_rate(rate: int):
        return 0 <= rate <= 5

    def _is_amount_valid(self, amount: float):
        return amount > 0

    def _is_balance_valid(self, balance: float, amount: float):
        return (balance - amount) > BankAccount.MIN_BALANCE

    def _log_transaction(self, transaction_type: str, amount: float):
        print(f"{datetime.now()}: {transaction_type} an amount of ${amount}")


# account1 = BankAccount("Yaw", 500)
# result = account1.deposit(20)
# print(result)
# result = account1.withdraw(110)
# print(result)
# result = account1.withdraw(200)
# print(result)
# result = account1.withdraw(200)
# print(result)
# account1.withdraw(76)
# print(BankAccount.is_valid_interest_rate(10))
# print(BankAccount.is_valid_interest_rate(4))
