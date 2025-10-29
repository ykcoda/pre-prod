"""
Coupling
The degree of dependencies between different classes or modules within a system
"""

from abc import ABC, abstractmethod


class NotificationService(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class EmailService(NotificationService):
    def send_notification(self, message):
        print(f"Sending email: {message}")


class MobileService(NotificationService):
    def send_notification(self, message):
        print(f"Sending text message: {message}")


class Order:

    def __init__(self, notification_service: NotificationService):
        self.notification_service = notification_service

    def create(self):
        # Perform order creating logic, validate order details,
        # check product stock and save to database...
        self.notification_service.send_notification(
            "Hi, your order was placed successfuly and will be delivered within 2-5 working days."
        )


order1 = Order(MobileService())
order1.create()

order2 = Order(EmailService())
order2.create()
