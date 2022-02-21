import uuid

from picpay.application.client.create_client_dto import CreateClientDTO
from picpay.domain.client.client_type import ClientType
from picpay.domain.wallet.wallet import Wallet


class Client:
    id: uuid = uuid.uuid4()
    name: str
    document_number: str
    email: str
    password: str
    type: ClientType
    wallet: Wallet

    CPNJ_LENGTH = 14
    CPF_LENGTH = 11

    def __init__(self, name, document_number, email, password, type, wallet):
        self.name = name
        self.document_number = document_number
        self.email = email
        self.password = password
        self.type = type
        self.wallet = wallet

    @property
    def is_allowed_to_transfer(self) -> bool:
        if self.type == ClientType.COMUM:
            return True

        return False

    @classmethod
    def from_create_client_dto(cls, dto: CreateClientDTO):
        document_types = {
            cls.CPNJ_LENGTH: ClientType.MERCHANT,
            cls.CPF_LENGTH: ClientType.COMUM
        }

        document_type = document_types.get(len(dto.document_number))

        return cls(
            name=dto.name,
            document_number=dto.document_number,
            email=dto.email,
            password=dto.password,
            type=document_type,
            wallet=Wallet.create(client_id=cls.id, client_type=cls.type)
        )
