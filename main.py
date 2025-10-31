from account import BankAccount, AccountType
from customer import Customer


customer1 = Customer("Yaw", "Kyereh", "yawkyereh@gmail.com")
savings_account = BankAccount(AccountType.SAVINGS)
savings_account1 = BankAccount(AccountType.SAVINGS)
current_account = BankAccount(AccountType.CURRENT)

customer1.add_account(savings_account)
customer1.add_account(savings_account1)
customer1.add_account(current_account)

savings_account.deposit(40)
current_account.deposit(1400)

print("Accounts")
customer1.show_accounts()


print("closing account")
customer1.close_account(savings_account)
customer1.close_account(savings_account1)
customer1.close_account(current_account)

customer1.show_accounts()
