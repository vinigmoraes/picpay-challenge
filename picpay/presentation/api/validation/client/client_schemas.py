CREATE_CLIENT_REQUEST = {
    'name': {'type': 'string', 'empty': False},
    'document_number': {
        'type': 'string',
        'valid_document_number': True,
        'minlength': 11,
        'maxlength': 14
    },
    'email': {
        'type': 'string',
        'empty': False,
        'email': True
    },
    'password': {
        'type': 'string',
        'empty': False
    }
}
