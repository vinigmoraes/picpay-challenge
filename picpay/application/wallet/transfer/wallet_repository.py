from typing import Protocol, Optional

from picpay.domain.wallet.wallet import Wallet


class WalletRepository(Protocol):

    def find_by_client_id(self, client_id: str) -> Optional[Wallet]:
        ...
