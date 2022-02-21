from picpay.presentation.api.validation.wallet.wallet_schemas import TRANSFER_MONEY_REQUEST
from picpay.presentation.api.wallet.transfer_money.transfer_request import TransferMoneyRequest
from picpay.presentation.api.validation.request_validator import validate_request


class TransferMoneyController:

    def __init__(self, use_case: TransferMoneyUseCase):

    def transfer(self, request_body: TransferMoneyRequest):
        validate_request(request_body, TRANSFER_MONEY_REQUEST)

        return "Transfer executed successfully"
