import strawberry

from picpay.application.wallet.transfer.transfer_money_dto import TransferMoneyDTO


@strawberry.input
class TransferMoneyRequest:
    amount: int
    payer: str
    recipient: str

    def to_dto(self):
        return TransferMoneyDTO(
            amount=self.amount,
            payer=self.payer,
            recipient=self.recipient
        )
