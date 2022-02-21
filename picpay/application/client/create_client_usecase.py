from picpay.application.client.client_repository import ClientRepository
from picpay.application.client.create_client_dto import CreateClientDTO
from picpay.domain.client.client import Client


class CreateClientUseCase:

    def __init__(self, repository: ClientRepository):
        self.repository = repository

    def create(self, dto: CreateClientDTO) -> Client:
        client = self.repository.find_by_email(dto.email)

        if client:
            raise Exception(f"Client with email: {dto.email} already exists")

        client = Client.from_create_client_dto(dto)

        self.repository.save(client)

        return client
