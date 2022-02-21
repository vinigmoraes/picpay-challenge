import strawberry


@strawberry.input
class TransferMoneyRequest:
    amount: int
    payer: str
    recipient: str
