TRANSFER_MONEY_REQUEST = {
    'amount': {'type': 'number'},
    'recipient': {
        'is uuid': True,
        'type': 'string'
    },
    'payer': {
        'is uuid': True,
        'type': 'string'
    }
}
