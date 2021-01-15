from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status


def is_superuser(function):
    def wrap(*args, **kwargs):
        for arg in args:
            if isinstance(arg, Request) and arg.user.is_superuser:
                return function(*args, **kwargs)
        return Response(
            {"details": "Unauthorized"}, status=status.HTTP_401_UNAUTHORIZED
        )

    wrap.__name__ = function.__name__
    return wrap
