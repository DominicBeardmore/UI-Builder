import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class IntegerField:
    type: str = "integer"
    maximum: int = 0