import dataclasses
from pydantic.dataclasses import dataclass
from typing import Union

@dataclass
class StringField:
    type: str = "string"
    minLength: int = 1
 
@dataclass
class DateField:
    type: str = "string"
    format: str = "date"

@dataclass
class IntegerField:
    type: str = "integer"
    maximum: int = 0

@dataclass
class EnumField:
    type: str = "string"
    enum: list[str] = dataclasses.field(default_factory=lambda: [])

@dataclass
class BooleanField:
    type: str = "boolean"

@dataclass
class Schema:
    type: str=""
    properties: dict[str, Union[StringField, DateField, BooleanField, EnumField, IntegerField]] = None

@dataclass
class Ele:
    type: str=""
    scope: str=""
    label: str=""

@dataclass
class Layout:
    type: str = "VerticalLayout"
    elements: list[Ele] = dataclasses.field(default_factory=lambda: [0])
    
@dataclass
class Labels:
    string_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    date_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    enum_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    boolean_labels: list[str] = dataclasses.field(default_factory=lambda: [])
    integer_labels: list[str] = dataclasses.field(default_factory=lambda: [])