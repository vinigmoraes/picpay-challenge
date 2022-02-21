from typing import Protocol

from picpay.domain.wallet.wallet import Wallet


class WalletRepository(Protocol):

    def find_by_client_id(self, client_id: str) -> Wallet:
        ...
