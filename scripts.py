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
    def __init__(self):
        pass

    def register(self, user):
        print(f"Registring user {user.username}")

        email_sender = EmailSender()
        email_sender.send(user.email, f"Welcome to our platform, {user.username}!")

    def update(self, user):
        print(f"Updating user: {user.username}")

    def delete(self, user):
        print(f"Deleting user: {user.username}")


user1 = User("YK", "yk@gmail.com")
userService = UserService()
userService.register(user1)


user2 = User("Annie", "annie@gmail.com")
userService.register(user2)
