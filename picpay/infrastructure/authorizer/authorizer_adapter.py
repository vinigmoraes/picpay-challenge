import logging

import requests
from requests import Response

from picpay.infrastructure.authorizer.authorizer_exception import AuthorizerException


class AuthorizerAdapter:
    logger = logging.Logger(name="AuthorizerAdapter")

    def __init__(self, url):
        self.url = url

    def authorize(self):
        response: Response = requests.get(url=self.url)

        if not response.ok:
            raise AuthorizerException()
