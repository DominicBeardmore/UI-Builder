import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class EnumField:
    type: str = "string"
    enum: list[str] = dataclasses.field(default_factory=lambda: [])