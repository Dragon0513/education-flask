from enum import Enum


class Permissions(Enum):
    READ = "read"
    WRITE = "write"
    DELETE = "delete"
    ADMIN = "admin"
    # add other permissions as needed
