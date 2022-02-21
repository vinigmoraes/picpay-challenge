import strawberry

from picpay.application.client.create_client_usecase import CreateClientUseCase
from picpay.infrastructure.client.client_repository_adapter import ClientRepositoryAdapter
from picpay.presentation.api.client.client_created_response import ClientCreatedResponse
from picpay.presentation.api.client.create_client_controller import CreateClientController
from picpay.presentation.api.client.create_client_request import CreateClientRequest
from picpay.presentation.api.wallet.transfer_money.transfer_money_controller import TransferMoneyController
from picpay.presentation.api.wallet.transfer_money.transfer_request import TransferMoneyRequest


@strawberry.type
class Mutations:

    @strawberry.mutation
    def transfer_money(self, request: TransferMoneyRequest) -> str:
        controller = TransferMoneyController()
        return controller.transfer(request)

    @strawberry.mutation
    def create_client(self, request: CreateClientRequest) -> ClientCreatedResponse:
        controller = CreateClientController(CreateClientUseCase(ClientRepositoryAdapter()))

        return controller.create(request)
