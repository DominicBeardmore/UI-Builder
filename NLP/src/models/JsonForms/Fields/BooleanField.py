import dataclasses
from pydantic.dataclasses import dataclass

@dataclass
class BooleanField:
    type: str = "boolean"