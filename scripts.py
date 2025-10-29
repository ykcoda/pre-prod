"""
Coupling
The degree of dependencies between different classes or modules within a system
"""


class EmailSender:

    def send(self, message):
        print(f"Sending email: {message}")


class Order:

    def create(self):
        # Perform order creating logic, validate order details,
        # check product stock and save to database...
        email = EmailSender()
        email.send(
            "Hi your order was placed succesfully and will be with you within 2-5 working days"
        )


order1 = Order()
order1.create()