from picpay.application.client.create_client_usecase import CreateClientUseCase
from picpay.presentation.api.client.client_created_response import ClientCreatedResponse
from picpay.presentation.api.client.create_client_request import CreateClientRequest
from picpay.presentation.api.validation.client.client_schemas import CREATE_CLIENT_REQUEST
from picpay.presentation.api.validation.request_validator import validate_request


class CreateClientController:

    def __init__(self, use_case: CreateClientUseCase):
        self.use_case = use_case

    def create(self, request_body: CreateClientRequest) -> ClientCreatedResponse:
        validate_request(request_body, CREATE_CLIENT_REQUEST)

        dto = request_body.to_dto()

        client = self.use_case.create(dto)

        return ClientCreatedResponse.from_client(client)
