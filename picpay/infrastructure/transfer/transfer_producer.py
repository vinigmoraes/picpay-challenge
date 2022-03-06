import pika

from picpay.domain.wallet.transfer.money_transfer import TransferMoney
from picpay.infrastructure.transfer.transfer_event import TransferEvent


class TransferProducerAdapter:

    def __init__(self, queue: str, host: str):
        self.queue = queue
        credentials = pika.PlainCredentials(username="admin", password="admin")
        self.producer = pika.BlockingConnection(pika.ConnectionParameters(host=host, credentials=credentials)).channel()
        self.producer.queue_declare(queue)

    def publish(self, transfer: TransferMoney):
        event = TransferEvent(
            id=transfer.id,
            payer=transfer.payer,
            recipient=transfer.recipient,
            amount=transfer.amount
        )

        self.producer.basic_publish(
            exchange='',
            routing_key=self.queue,
            body=event.to_json()
        )

        self.producer.close()
