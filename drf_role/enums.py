from enum import Enum


class PermissionEnum(Enum):
    READ = 0
    WRITE = 1
    NO_ACCESS = 2


class RoleEnum(Enum):
    Admin = 0
