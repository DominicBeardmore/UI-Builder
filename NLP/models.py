import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class StrEle:
    type: str="string"
    minLength: int = 1

@dataclass
class Schema:
    type: str=""
    properties: dict[str, StrEle] = None

@dataclass
class Ele:
    type: str=""
    scope: str=""
    label: str=""

@dataclass
class Layout:
    type: str = "VerticalLayout"
    elements: list[Ele] = dataclasses.field(default_factory=lambda: [0])