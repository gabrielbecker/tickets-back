from rest_framework.exceptions import APIException
from rest_framework.status import HTTP_406_NOT_ACCEPTABLE, HTTP_500_INTERNAL_SERVER_ERROR


class TicketsException(APIException):
    def __init__(self, error=None, data=None, status_code=HTTP_406_NOT_ACCEPTABLE):
        super().__init__(data)
        self.error = error
        self.data = data
        self.detail = {'message': error, 'data': data}
        self.status_code = status_code

    def __str__(self):
        import json
        return json.dumps(self.detail)


class TicketsInternalServerException(APIException):

    def __init__(self, debug_info, error='An internal error occurred. Please contact system admin', data=None):
        super().__init__(data)
        self.error = error
        self.data = data
        self.debug_info = debug_info
        self.detail = {'message': error, 'data': data}
        self.status_code = HTTP_500_INTERNAL_SERVER_ERROR

    def __str__(self):
        import json
        return json.dumps(self.detail)
