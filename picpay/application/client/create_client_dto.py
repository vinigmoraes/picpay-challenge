import dataclasses


@dataclasses.dataclass
class CreateClientDTO:
    name: str
    document_number: str
    email: str
    password: str
