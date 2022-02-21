import strawberry

from picpay.application.client.create_client_usecase import CreateClientUseCase
from picpay.infrastructure.client.client_repository_adapter import ClientRepositoryAdapter
from picpay.presentation.api.client.client_created_response import ClientCreatedResponse
from picpay.presentation.api.client.create_client_controller import CreateClientController
from picpay.presentation.api.client.create_client_request import CreateClientRequest


@strawberry.type
class ClientMutation:

    @strawberry.mutation
    def create(self, request: CreateClientRequest) -> ClientCreatedResponse:
        controller = CreateClientController(CreateClientUseCase(ClientRepositoryAdapter()))

        return controller.create(request)
