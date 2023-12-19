import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class StringField:
    type: str = "string"
    minLength: int = 1
