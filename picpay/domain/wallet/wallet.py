import uuid
from decimal import Decimal

from picpay.domain.client.client_type import ClientType


class Wallet:
    id: uuid = uuid.uuid4()
    client_id: uuid
    balance: Decimal = 0
    can_transfer: bool

    def __init__(self, client_id, can_transfer):
        self.client_id = client_id
        self.can_transfer = can_transfer

    def has_balance(self, value) -> bool:
        if self.balance >= value:
            return True

        return False

    def transfer(self, value):
        self.balance = self.balance - value

    def deposit(self, value):
        self.balance = self.balance + value

    @classmethod
    def create(cls, client_id: uuid, client_type: ClientType):
        can_transfer = False

        if client_type == ClientType.COMUM:
            can_transfer = True

        return cls(
            client_id=client_id,
            can_transfer=can_transfer
        )
