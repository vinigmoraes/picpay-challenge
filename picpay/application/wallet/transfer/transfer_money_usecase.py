from picpay.application.wallet.transfer.transfer_money_dto import TransferMoneyDTO
from picpay.application.wallet.transfer.wallet_repository import WalletRepository


class TransferMoneyUseCase:

    def __init__(self, repository: WalletRepository):
        self.repository = repository

    def execute(self, transfer_money_dto: TransferMoneyDTO):
        wallet = self.repository.find_by_client_id(transfer_money_dto.payer)

        if not wallet.has_balance() or not wallet.can_transfer:
            raise Exception()









