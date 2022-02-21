from typing import Protocol, Optional

from picpay.domain.client.client import Client


class ClientRepository(Protocol):

    def save(self, client: Client):
        ...

    def find_by_email(self, email) -> Optional[Client]:
        ...
