import dataclasses


@dataclasses.dataclass
class TransferMoneyDTO:
    amount: int
    payer: str
    recipient: str
