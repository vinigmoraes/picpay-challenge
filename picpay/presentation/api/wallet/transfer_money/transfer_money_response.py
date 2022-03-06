import dataclasses
from datetime import datetime

import strawberry

from picpay.domain.wallet.transfer.money_transfer import TransferMoney


@strawberry.type
class TransferMoneyResponse:
    payer: str
    recipient: str
    amount: int
    created_at: datetime
    id: str

    def __init__(self, payer: str, amount: int, recipient: str, created_at: datetime, id: str):
        self.id = id
        self.payer = payer
        self.amount = amount
        self.recipient = recipient
        self.created_at = created_at

    @classmethod
    def create(cls, transfer_money: TransferMoney):
        return cls(
            payer=transfer_money.payer,
            amount=transfer_money.amount,
            recipient=transfer_money.recipient,
            created_at=transfer_money.created_at,
            id=str(transfer_money.id)
        )
