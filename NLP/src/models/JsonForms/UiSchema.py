import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class Ele:
    type: str=""
    scope: str=""
    label: str=""

@dataclass
class UiSchema:
    type: str = ""
    elements: list[Ele] = dataclasses.field(default_factory=lambda: [0])
    