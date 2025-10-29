"""
Abstraction
Reduce complexity by hiding unnecessary details
"""

class EmailService:
    def _connect(self):
        print("connecting to email server")

    def _authenticate(self):
        print("authenticating...")

    def send_email(self, message: str):
        self._connect()
        self._authenticate()
        print(f"Email Sent: '{message}'")
        self._disconnect()

    def _disconnect(self):
        print("disconnecting from email server.")


message1 = EmailService()
message1.send_email("I love python programming....")