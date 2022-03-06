import uuid
from typing import Optional

from picpay.application.wallet.transfer.wallet_repository import WalletRepository
from picpay.domain.client.client_type import ClientType
from picpay.domain.wallet.wallet import Wallet


class WalletRepositoryAdapter(WalletRepository):
    wallets = [
        Wallet.create(client_id=uuid.UUID("1f995cd5-b07c-4dcd-83d0-d391c0b85644"),
                      client_type=ClientType.COMUM)
    ]

    def find_by_client_id(self, client_id: str) -> Optional[Wallet]:
        for wallet in self.wallets:
            if str(wallet.client_id) == client_id:
                wallet.deposit(500)
                return wallet

        return None
