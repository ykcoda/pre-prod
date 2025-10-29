"""
S: Single Responsibility Principle (SRP)
A class should have only one reason to change, meaning that it should have only one
responsibility or purpose
"""

class EmailSender:
    def send(self, recipient, message):
        print(f"Sending email to {recipient}: {message}")


class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email

    def register(self):
        print(f"Registring user {self.username}")

        email_sender = EmailSender()
        email_sender.send(self.email, f"Welcome to our platform {self.username}!")


user1 = User("YK", "yk@gmail.com")
user1.register()