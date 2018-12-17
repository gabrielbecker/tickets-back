import sys
import logging
from django.db.utils import DatabaseError
from django.utils.translation import ugettext
from rest_framework.views import exception_handler
from rest_framework import exceptions

from utils.custom_exceptions import TicketsInternalServerException


def custom_exception_handler(exc, context):
    """ Overriding Django rest framework's custom exception """

    # Log exception if not in test runner
    if len(sys.argv) > 1 and sys.argv[1] != 'test':
        logger = logging.getLogger(__name__)

        if hasattr(exc, 'detail'):
            logger.exception(exc.detail)
        else:
            logger.exception(exc)

        if hasattr(exc, 'debug_info'):
            logger.exception('DEV-INFO', exc.debug_info)

    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if response is not None:

        if isinstance(exc, (exceptions.NotAuthenticated, exceptions.PermissionDenied)):
            return response

        if not isinstance(exc, exceptions.APIException):
            response.data['status_code'] = response.status_code

    # Catching database error
    if exc and isinstance(exc, DatabaseError):
        raise TicketsInternalServerException(debug_info=ugettext('Database error'))
    return response


class RequestUtils:

    @classmethod
    def is_admin_or_api_docs(cls, request):
        return True if cls.is_api_documentation(request) or cls.is_admin_module(request) else False

    @classmethod
    def is_api_documentation(cls, request):
        return True if '/docs' in request.path else False

    @classmethod
    def is_admin_module(cls, request):
        return True if '/admin/' in request.path else False
