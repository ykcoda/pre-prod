"""
S: Single Responsibility Principle (SRP) REFACTORING
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


class UserService:
    def register(self, user: User):
        print(f"Registring user {user.username}")

        email_sender = EmailSender()
        email_sender.send(user.email, f"Welcome to our platform, {user.username}!")

    def update(self, user: User):
        print(f"Updating user: {user}")

    def delete(self, user: User):
        print(f"Deleting user: {user}")
    
    
user1 = User("YK", "yk@gmail.com")  
userService = UserService()
userService.register(user1)

user2 = User("Annie", "annie@gmail.com")
userService1 = UserService()
userService1.register(user2)
