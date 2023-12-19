import dataclasses
from pydantic.dataclasses import dataclass
from .Fields import BooleanField, DateField, StringField, EnumField, IntegerField
from typing import Union

@dataclass
class Schema:
    type: str=""
    properties: dict[str, Union[StringField, DateField, BooleanField, EnumField, IntegerField]] = None
