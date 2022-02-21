import strawberry

from picpay.application.client.create_client_dto import CreateClientDTO


@strawberry.input
class CreateClientRequest:
    name: str
    document_number: str
    email: str
    password: str

    def to_dto(self):
        return CreateClientDTO(
            name=self.name,
            document_number=self.document_number,
            email=self.email,
            password=self.password
        )
