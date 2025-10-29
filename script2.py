from abc import ABC, abstractmethod


class NotificationService1(ABC):
    @abstractmethod
    def send_notification(self, message: str):
        pass


class EmailService(NotificationService1):
    def send_notification(self, message):
        print(f"sending email: {message}")


class FaxService(NotificationService1):
    def send_notification(self, message):
        print(f"sending fax: {message}")


class MobileService(NotificationService1):
    def send_notification(self, message):
        print(f"sending text: {message}")


class Order:

    def create(self, notification_service: NotificationService1):
        # implement logic

        notification_service.send_notification(
            "Hi order has been placed. You will receive order in 2-5 working days."
        )



order1 = Order()
order1.create(FaxService())    