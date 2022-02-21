class ValidationException(Exception):

    def __init__(self, errors):
        self.erros = errors

    status_code = 400

    def response(self):
        return {
            'errors': self.erros
        }
