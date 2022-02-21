import re

from cerberus import Validator
from email_validator import validate_email, EmailNotValidError
from pycpfcnpj import cpfcnpj

from picpay.presentation.api.validation.validation_exception import ValidationException


class RequestValidator(Validator):

    def _validate_is_uuid(self, is_uuid, field, value):
        """ Test if value is uuid.

            The rule's arguments are validated against this schema:
            {'type': 'boolean'}
        """
        re_uuid = re.compile(r'[0-9a-f]{8}(?:-[0-9a-f]{4}){3}-[0-9a-f]{12}', re.I)

        if is_uuid and not re_uuid.match(value):
            self._error(field, "Must be valid UUID")

    def _validate_valid_document_number(self, valid_document_number, field, value):
        """ Test if value is document number is valid.

            The rule's arguments are validated against this schema:
            {'type': 'boolean'}
        """
        if valid_document_number and not cpfcnpj.validate(value):
            self._error(field, f"Invalid document number: {value}")

    def _validate_email(self, valid_email, field, value):
        """ Test if value is valid_email.

            The rule's arguments are validated against this schema:
            {'type': 'boolean'}
        """

        is_valid = True
        try:
            validate_email(value)
        except EmailNotValidError as e:
            is_valid = False

        if valid_email and not is_valid:
            self._error(field, f"Invalid email address: {value}")


def validate_request(request, schema):
    validator = RequestValidator(schema)

    if not validator.validate(request.__dict__):
        raise ValidationException(validator.errors)
