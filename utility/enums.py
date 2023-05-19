from django_enumfield import enum
from enum import Enum


class StatusEnum(enum.Enum):
    OPENED = 1
    CLOSED = 2


class OrderFileTypeEnum(Enum):
    pdf = "pdf"
    excel = "excel"


class StatusUtils(str, Enum):
    success = "success"
    fail = "fail"
    not_found = "not_found"
