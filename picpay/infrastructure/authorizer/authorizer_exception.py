class AuthorizerException(Exception):
    message: str

    def __init__(self):
        super().__init__(self.message)
