"""
Behavioral: The interaction or communication between those objects
"""

from enum import Enum


class DocumentState(Enum):
    DRAFT = 1
    MODERATION = 2
    PUBLISHED = 3


class UserRoles(Enum):
    READER = 1
    EDITOR = 2
    ADMIN = 3


class Document:

    def __init__(self, state: DocumentState, current_user_role: UserRoles):
        self.state = state
        self.current_user_role = current_user_role

    def publish(self):
        if self.state == DocumentState.DRAFT:
            self.state = DocumentState.MODERATION

        elif (
            self.state == DocumentState.MODERATION
            and self.current_user_role == UserRoles.ADMIN
        ):
            self.state = DocumentState.PUBLISHED

        elif self.state == DocumentState.PUBLISHED:
            # Do nothing
            pass


doc = Document(DocumentState.DRAFT, UserRoles.EDITOR)
print(f"Initial state: {doc.state.name}")

doc.publish()
print(f"Initial state: {doc.state.name}")

doc.publish()
print(f"Initial state: {doc.state.name}")