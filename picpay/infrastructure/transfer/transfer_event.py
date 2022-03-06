from dataclasses import dataclass
from dataclasses_json import dataclass_json


@dataclass_json
@dataclass
class TransferEvent:
    id: str
    payer: str
    recipient: str
    amount: int
