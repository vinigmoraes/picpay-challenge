from picpay.application.wallet.transfer.transfer_money_dto import TransferMoneyDTO
from picpay.application.wallet.transfer.wallet_repository import WalletRepository
from picpay.domain.wallet.transfer.money_transfer import TransferMoney
from picpay.infrastructure.authorizer.authorizer_adapter import AuthorizerAdapter
from picpay.infrastructure.authorizer.authorizer_exception import AuthorizerException
from picpay.infrastructure.transfer.transfer_producer import TransferProducerAdapter


class TransferMoneyUseCase:

    def __init__(self, repository: WalletRepository):
        self.repository = repository
        self.authorizer = AuthorizerAdapter(
            url="https://run.mocky.io/v3/8fafdd68-a090-496f-8c9a-3442cf30dae6"
        )
        self.producer = TransferProducerAdapter(
            host="localhost",
            queue="transfer_money"
        )
        self.producer = TransferProducerAdapter(
            queue="transfer_money",
            host="localhost"
        )

    def execute(self, transfer_money_dto: TransferMoneyDTO) -> TransferMoney:
        payer_wallet = self.repository.find_by_client_id(transfer_money_dto.payer)

        if not payer_wallet.can_transfer:
            raise Exception(f"Wallet: {payer_wallet.id} not authorized to execute transfer")

        if not payer_wallet.has_balance(transfer_money_dto.amount):
            raise Exception("Wallet hasn't enough balance")

        try:
            payer_wallet.transfer(transfer_money_dto.amount)

            self.authorizer.authorize()

            transfer = TransferMoney.create(dto=transfer_money_dto)

            self.producer.publish(transfer)

            return transfer

        except AuthorizerException as e:
            payer_wallet.deposit(transfer_money_dto.amount)

            raise Exception("Error when transfer money")




















