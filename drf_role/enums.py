from enum import Enum


class PermissionEnum(Enum):
    """
        These are not http status code. Code just designed as like as http status code
    """
    GET = 200
    POST = 201
    PUT = 202
    PATCH = 203
    DELETE = 204
    NO_ACCESS = 403


class RoleEnum(Enum):
    Admin = 0
