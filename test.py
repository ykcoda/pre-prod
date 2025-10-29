from BankAccount import BankAccount
from Customer import Customer


customer1 = Customer("Emmanuel", "emma@yahoo.com")
customer1BA = BankAccount(customer1, 350)
customer1BA.withdraw(900)
customer1BA.deposit(43.89)
customer1BA.withdraw(129.12)
customer1BA.deposit(900.89)
customer1BA.withdraw(1200)


