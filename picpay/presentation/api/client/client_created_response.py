import strawberry

from picpay.domain.client.client import Client


@strawberry.type
class ClientCreatedResponse:
    id: str

    def __init__(self, id: str):
        self.id = id

    @classmethod
    def from_client(cls, client: Client):
        return cls(
            id=str(client.id)
        )
