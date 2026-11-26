from rest_framework.views import exception_handler as drf_exception_handler
from rest_framework.response import Response

from .exceptions import BibliotecaException


def custom_exception_handler(exc, context):
    if isinstance(exc, BibliotecaException):
        return Response(
            {"erro": exc.message},
            status=exc.status_code,
        )

    
    response = drf_exception_handler(exc, context)

    if response is None:
        
        return Response(
            {"erro": "Ocorreu um erro interno no servidor."},
            status=500,
        )

    return response