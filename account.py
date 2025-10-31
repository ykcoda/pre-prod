from datetime import datetime  # noqa
from enum import Enum
from uuid import UUID, uuid4


class AccountType(str, Enum):
    CURRENT = "current"
    SAVINGS = "savings"


class BankAccount:

    MIN_BALANCE = 100

    def __init__(self, account_type: AccountType = AccountType.CURRENT):
        self.id: UUID = uuid4()
        self.balance: float = 0.0
        self.account_type = account_type

    def _is_amount_valid(self, amount: float):
        return amount > 0

    def deposit(self, amount: float):
        if not self._is_amount_valid(amount):
            print(f"${amount} is an valid amount")
            return
        self.balance += amount
        print(f"You deposited ${amount}, your new balance is ${self.balance}")

    def withdraw(self, amount: float):
        if not self._is_amount_valid(amount):
            print(f"${amount} is an valid amount")
            return
        self.balance -= amount
        print(f"You withdrew ${amount}, your new balance is ${self.balance}")
