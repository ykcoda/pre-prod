from uuid import UUID, uuid4
from datetime import datetime
from typing import TYPE_CHECKING
from account import BankAccount

if TYPE_CHECKING:
    from .account import BankAccount


class Customer:

    def __init__(self, firstname: str, lastname: str, email: str):
        self.id: UUID = uuid4()
        self.firstname: str = firstname
        self.lastname: str = lastname
        self.email: str = email
        self.created_at: datetime = datetime.now()
        self.bank_accounts: list["BankAccount"] = []

    def add_account(self, account: BankAccount):
        self.bank_accounts.append(account)

    def show_accounts(self):
        for account in self.bank_accounts:
            print(f"{account.account_type} account: ${account.balance}")

    def close_account(self, account: BankAccount):
        for acc in self.bank_accounts:
            if acc.id == account.id:
                self.bank_accounts.remove(acc)
