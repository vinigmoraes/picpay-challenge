from typing import Optional

from picpay.application.client.client_repository import ClientRepository
from picpay.domain.client.client import Client


class ClientRepositoryAdapter(ClientRepository):

    clients = []

    def save(self, client):
        self.clients.append(client)

    def find_by_email(self, email) -> Optional[Client]:
        for client in self.clients:
            if client.email == email:
                return client

        return None


