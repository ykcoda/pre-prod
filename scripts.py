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
    def __init__(self, user: User):
        self.user = user

    def register(self):
        print(f"Registring user {self.user.username}")
        
        email_sender = EmailSender()
        email_sender.send(
            self.user.email, f"Welcome to our platform, {self.user.username}!"
        )

    def update(
        self,
    ):
        print(f"Updating user: {self.user.username}")

    def delete(self):
        print(f"Deleting user: {self.user.username}")


user1 = User("YK", "yk@gmail.com")
userService1 = UserService(user1)
userService1.register()
userService1.update()
userService1.delete()


user2 = User("Annie", "annie@gmail.com")
userService2 = UserService(user2)
userService2.register()
userService2.update()
