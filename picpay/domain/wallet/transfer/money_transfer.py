import dataclasses
import uuid
from datetime import datetime

from picpay.application.wallet.transfer.transfer_money_dto import TransferMoneyDTO


@dataclasses.dataclass
class TransferMoney:
    payer: str
    recipient: str
    amount: int
    created_at: datetime
    id: uuid = uuid.uuid4()

    @classmethod
    def create(cls, dto: TransferMoneyDTO):
        return cls(
            payer=dto.payer,
            recipient=dto.recipient,
            amount=dto.amount,
            created_at=datetime.now()
        )
